# coding: utf-8
from sqlalchemy import Column, DECIMAL, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Brand(Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True, unique=True)
    brand_name = Column(String(100), nullable=False, unique=True)
    brand_code = Column(String(3), nullable=False, unique=True)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, unique=True)
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(100), nullable=False)
    user_password = Column(String(255), nullable=False)


class Model(Base):
    __tablename__ = 'models'

    model_id = Column(Integer, primary_key=True, unique=True)
    model_name = Column(String(100), nullable=False, unique=True)
    model_code = Column(String(3), nullable=False, unique=True)
    brand_code = Column(ForeignKey('brands.brand_code'), index=True)

    brand = relationship('Brand')


class Part(Base):
    __tablename__ = 'parts'

    part_id = Column(Integer, primary_key=True, unique=True)
    part_name = Column(String(100), nullable=False, unique=True)
    part_code = Column(String(3), nullable=False, unique=True)
    part_price = Column(DECIMAL(10, 0), nullable=False)
    part_amount = Column(Integer, nullable=False)
    model_code = Column(ForeignKey('models.model_code'), index=True)

    model = relationship('Model')
