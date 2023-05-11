#!/usr/bin/python3
""" a module that defines the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ a class that defines a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
