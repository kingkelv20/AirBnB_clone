#!/usr/bin/python3
""" a module that defines the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ defines the city """
    state_id = ""
    name = ""
