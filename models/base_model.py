#!/usr/bin/env python3
# this module contain definition of the class BaseModel

import uuid
import datetime


class BaseModel():
    """ defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ initialises all attributes"""

        if (kwargs):
            # assign kwargd key and values to the object
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            self.created_at = datetime.datetime.strptime(
                              kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(
                              kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """ returns the descriprion of the object
            format: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at,
            with the current datetime"""

        self.updated_at = datetime.datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """  returns a dictionary containing all keys/values
             of __dict__ of the instance"""

        dictionary = {}
        dictionary["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if (key == "created_at"):
                dictionary[key] = self.created_at.isoformat()
            elif (key == "updated_at"):
                dictionary[key] = self.updated_at.isoformat()
            else:
                dictionary[key] = value
        return dictionary
