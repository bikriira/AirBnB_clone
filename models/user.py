#!/usr/bin/python3

from .base_model import BaseModel
"""Define User class."""


class User(BaseModel):
    """A class representing a user entity."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
