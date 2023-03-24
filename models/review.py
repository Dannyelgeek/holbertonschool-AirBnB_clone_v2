#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
import os


class Review(BaseModel, Base if os.getenv('HBNB_TYPE_STORAGE') == 'db'
             else object):
    """ Review class to store review information """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "reviews"

        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
