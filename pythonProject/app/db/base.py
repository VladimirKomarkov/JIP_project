from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('postgresql+psycopg2://jip_user:jip_password@localhost:5432/jip_database')
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
