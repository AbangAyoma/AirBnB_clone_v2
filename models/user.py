#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import models
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if type_of_storage = 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable-False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super.()__init__(*args, **kwargs)
