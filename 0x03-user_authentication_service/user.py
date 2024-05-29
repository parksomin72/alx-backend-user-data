#!/usr/bin/env python3
"""
User model for user authentication service.
"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    SQLAlchemy model for the users table.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)

if __name__ == "__main__":
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)
