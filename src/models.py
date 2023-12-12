import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    favorites = relationship('Favorite', back_populates='user')

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    population = Column(Integer)
    characters = relationship('Character')

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='favorites')
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
