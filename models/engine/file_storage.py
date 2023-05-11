#!/usr/bin/python3
"""
    file_storage that handles serialzation and deserialziation of JSON objects
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ it takes care of serialization, deserialization,
    loading objects from a file, saving objects to a file """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns all objects in the __objects class attribute"""
        return FileStorage.__objects

    def new(self, obj):
        """ adds a new object to the __objects class attribut """
        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ saves the objects in a file using __file_path"""
        temp = {f: FileStorage.__objects[f].to_dict()
                for f in FileStorage.__objects}
        js = json.dumps(temp)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(js)

    def reload(self):
        """ reloads the content inside the the file stated in __file_path """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                js = f.read()
                temp = json.loads(js)
                FileStorage.__objects = {}
                for t in temp:
                    a = eval(temp[t]['__class__'])(**temp[t])
                    self.new(a)
