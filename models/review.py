#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if type_of_storage == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('user.id'))
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initializes review"""
        super().__init__(*args, **kwargs)
