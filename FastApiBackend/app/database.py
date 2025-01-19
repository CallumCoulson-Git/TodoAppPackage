from sqlmodel import SQLModel, create_engine, Session
from app.models import User, Reserve
from datetime import datetime
import bcrypt

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_dummy_data(session: Session = None):
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
