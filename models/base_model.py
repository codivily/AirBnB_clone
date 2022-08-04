#!/usr/bin/env python3
"""`BaseModel` class module that defines all common attributs/methods
for other classes
"""
from uuid import uuid4
from datetime import datetime, timezone

class BaseModel:
    """The base model class"""

    def __init__(self, *args, **kwargs):
        """Initialize an instance of `BaseModel` class

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        now = datetime.now(timezone.utc)
        self.created_at = now
        self.updated_at = now
        if (kwargs):
            for k, v in kwargs.items():
                if k is not "__class__":
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(v, tform)
                    else:
                        self.__dict__[k] = v

    def __str__(self):
        """Returns a string representation of `BaseModel` instance"""
        s = "[{}] ({}) {}".format("BaseModel", self.id, str(self.__dict__))
        return s


    def save(self):
        """
        Updates the public instance method updated_at with current datetime
        """
        self.updated_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        """Returns a dictionnary containing all keys/values of __dict__ """
        r = {}
        r["__class__"] = self.__class__.__name__

        for key in self.__dict__.keys():
            value = self.__dict__[key]
            if type(value) is datetime:
                r[key] = value.isoformat()
            else:
                r[key]= value

        return (r)

if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of  my_model_json:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
