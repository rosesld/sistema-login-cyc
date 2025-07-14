from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    rol = Column(String, nullable=False)
    renta_mensual = Column(Float, nullable=False)