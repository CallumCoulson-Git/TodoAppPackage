from typing import Union, Optional, List
from fastapi import FastAPI, Depends, Query, HTTPException,status, Form
from sqlmodel import SQLModel, Field, create_engine, Session, Relationship, select
from pydantic import EmailStr, validator, BaseModel
from datetime import datetime, timedelta
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware

import bcrypt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True, index=True)
    created_at: datetime = Field(default_factory=datetime.now, index=True)
    hashed_password: str
    is_active: bool
    reserves: Optional[List["Reserve"]] = Relationship(back_populates="owner", cascade_delete=True)

    class Config:
        arbitrary_types_allowed = True

class Reserve(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.now, index=True)
    set_for: Optional[datetime] = Field(default=None, index=True)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    owner: Optional[User] = Relationship(back_populates="reserves")
    @validator('set_for', pre=True, always=True)
    def parse_set_for(cls, value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value

    class Config:
        arbitrary_types_allowed = True





class Token(BaseModel):
    access_token: str
    token_type: str
    user: User
    
class TokenData(BaseModel):
    username: Optional[str] = None

class UserInDB(BaseModel):
    db_hashed_password: str

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_password_hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def authenticate_user(session: Session, email: str, password: str):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


######

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_dummy_data(session: Optional[Session] = None):
    with Session(engine) as session:
        password = "testpassword"
        user_1 = User(
            email="test@test.com",
            hashed_password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            is_active=True,
        )
        session.add(user_1)

        reserve_1 = Reserve(
            title="Reserve 1",
            set_for=datetime.now(),
            owner=user_1,
        )
        session.add(reserve_1)
        session.commit()
        session.close()



SessionDep = Depends(get_session)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    create_db_and_tables()
    create_dummy_data()


async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email)
    except JWTError:
        raise credentials_exception
    user = session.exec(select(User).where(User.email == token_data.username)).first()
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user




@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user": user}

@app.post("/user/", response_model=User)
def create_user(user: User, session:  Annotated[Session, SessionDep]):
    user.hashed_password = get_password_hash(user.hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/user/")
def read_users(
    session: Annotated[Session, SessionDep],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

@app.get("/user/{user_id}")
def read_user(user_id: int, session: Annotated[Session, SessionDep]) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/user/{user_id}")
def update_user(user_id: int, updated_user: User, session: Annotated[Session, SessionDep]) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = updated_user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.delete("/user/delete/{user_id}")
def delete_user(user_id: int, session: Annotated[Session, SessionDep]): 
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User and associated reserves deleted successfully"}

####

@app.post("/login/")
def login(email: Annotated[str, Form()], password: Annotated[str, Form()], session: Annotated[Session, SessionDep]
) -> User:
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return user


####


@app.post("/create_dummy_data/")
def create_dummy_data_api():
    create_dummy_data()
    return {"message": "Dummy data created"}


####


@app.post("/reserve/")
def create_reserve(reserve: Reserve, user_id: int, session: Annotated[Session, SessionDep]) -> Reserve:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if isinstance(reserve.set_for, str):
        reserve.set_for = datetime.fromisoformat(reserve.set_for)
    reserve.owner = user
    session.add(reserve)
    session.commit()
    session.refresh(reserve)
    return reserve

@app.get("/reserve/")
def read_reserves(
    session: Annotated[Session, SessionDep],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Reserve]:
    reserves = session.exec(select(Reserve).offset(offset).limit(limit)).all()
    return reserves

@app.get("/reserve/{reserve_id}")
def read_reserve(reserve_id: int, session: Annotated[Session, SessionDep]) -> Reserve:
    reserve = session.get(Reserve, reserve_id)
    if not reserve:
        raise HTTPException(status_code=404, detail="Reserve not found")
    return reserve

@app.get("/user/{user_id}/reserves")
def read_user_reserves(user_id: int, session: Annotated[Session, SessionDep]) -> list[Reserve]:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.reserves

@app.put("/reserve/{reserve_id}")
def update_reserve(reserve_id: int, updated_reserve: Reserve, session: Annotated[Session, SessionDep]) -> Reserve:
    reserve = session.get(Reserve, reserve_id)
    if not reserve:
        raise HTTPException(status_code=404, detail="Reserve not found")
    reserve_data = updated_reserve.dict(exclude_unset=True)
    for key, value in reserve_data.items():
        setattr(reserve, key, value)
    session.add(reserve)
    session.commit()
    session.refresh(reserve)
    return reserve

@app.delete("/reserve/{reserve_id}")
def delete_reserve(reserve_id: int, session: Annotated[Session, SessionDep]):
    reserve = session.get(Reserve, reserve_id)
    if not reserve:
        raise HTTPException(status_code=404, detail="Reserve not found")
    session.delete(reserve)
    session.commit()
    return {"message": "Reserve deleted successfully"}