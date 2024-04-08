# Add any model classes for Flask-SQLAlchemy here

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .__init__ import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    poster = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', poster='{self.poster}')>"
