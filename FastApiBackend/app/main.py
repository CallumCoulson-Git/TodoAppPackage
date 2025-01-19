# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables, create_dummy_data
from app.routers import user, reserve, auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    create_dummy_data()

app.include_router(user.router)
app.include_router(reserve.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}