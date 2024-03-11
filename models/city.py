#!/usr/bin/python3
"""
Module for City class.
"""
from .base_model import BaseModel
from .state import State


class City(BaseModel):
    """
    City class inherits from BaseModel.
    """

    self.state_id = ""
    self.name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes City instance.
        """
        super().__init__(*args, **kwargs)
