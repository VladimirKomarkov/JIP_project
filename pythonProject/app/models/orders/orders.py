from app.db.base import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    total_price = Column(Float)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))