from sqlalchemy import Column, Integer, String, Float
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()

class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)