"""
Simple module for managing database.
"""
from models import (
    Proficiency
)


from app_config import db

db.create_all()
