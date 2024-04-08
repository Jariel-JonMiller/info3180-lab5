# Add any model classes for Flask-SQLAlchemy here

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    poster = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', poster='{self.poster}')>"
