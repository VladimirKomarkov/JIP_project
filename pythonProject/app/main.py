from fastapi import FastAPI
from app.db.base import engine, Base


app = FastAPI()

@app.on_event('startup')
async def startup():
    Base.metadata.create_all(bind=engine)


@app.get('/')
async def read_root():
    return {"Hello": "World"}