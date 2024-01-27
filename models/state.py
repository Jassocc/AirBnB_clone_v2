#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import Base
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities_rel = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")

    @property
    def cities(self):
        """
        def class
        """
        variable = models.storage.all("City")
        city_list = []
        for city in variable.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
