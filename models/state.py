#!/usr/bin/python3
"""
Module for State class.
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes State instance.
        """
        super().__init__(*args, **kwargs)
