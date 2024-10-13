from db import engine, User
from fastapi import FastAPI
from datetime import date

from contextlib import asynccontextmanager
from sqlmodel import Session

@asynccontextmanager
async def lifespan(app: FastAPI):

    # define some users
    users = [
        User(id=1, name="John", dob=date(1990,1,1)),
        User(id=2, name="Jack", dob=date(1990,1,1)),
        User(id=3, name="Jill", dob=date(1990,1,1)),
        User(id=4, name="Jane", dob=date(1990,1,1)),
    ]

    with Session(engine) as session:
        for user in users:
            db_user = session.get(User, user.id)
            if db_user is not None:
                continue
            session.add(user)
        session.commit()
    yield

app = FastAPI(lifespan=lifespan)
  