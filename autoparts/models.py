# coding: utf-8
from sqlalchemy import Column, DECIMAL, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255), nullable=False, unique=True)
    code = Column(String(3), nullable=False, unique=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255), nullable=False, unique=True)
    code = Column(String(3), nullable=False, unique=True)
    brand_code = Column(ForeignKey('brands.code'), index=True)

    brand = relationship('Brand')


class Part(Base):
    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255), nullable=False, unique=True)
    code = Column(String(3), nullable=False, unique=True)
    price = Column(DECIMAL(10, 0), nullable=False)
    amount = Column(Integer, nullable=False)
    model_code = Column(ForeignKey('models.code'), index=True)

    model = relationship('Model')
