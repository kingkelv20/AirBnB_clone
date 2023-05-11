#!/usr/bin/python3
""" a module for the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ handles the reviews of users """
    place_id = ""
    user_id = ""
    text = ""
