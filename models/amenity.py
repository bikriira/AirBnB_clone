#!/usr/bin/python3
"""
Module for State class.
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes State instance.
        """
        super().__init__(*args, **kwargs)
