#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
import os
from models.city import City
import models


class State(BaseModel, Base if os.getenv('HBNB_TYPE_STORAGE') == 'db'
            else object):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)

        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            ''' return the list of City objects from storage
             linked to the current State'''
            city_dict = models.storage.all(City)
            city_list = []
            for k, v in city_dict.items():
                if v.state_id == self.id:
                    city_list.append(v)
            return city_list
