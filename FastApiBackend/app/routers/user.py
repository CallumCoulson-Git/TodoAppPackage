from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing_extensions import Annotated
from app.database import get_session
from app.models import User
from app.routers.auth import get_current_active_user

router = APIRouter()

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.post("/user/", response_model=User)
def create_user(user: User, session: Annotated[Session, Depends(get_session)]):
    user.hashed_password = get_password_hash(user.hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/user/")
def read_users(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

@router.get("/user/{user_id}")
def read_user(user_id: int, session: Annotated[Session, Depends(get_session)]) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/user/{user_id}")
def update_user(user_id: int, updated_user: User, session: Annotated[Session, Depends(get_session)]) -> User:
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

@router.delete("/user/delete/{user_id}")
def delete_user(user_id: int, session: Annotated[Session, Depends(get_session)]): 
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User and associated reserves deleted successfully"}
