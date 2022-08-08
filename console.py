#!/usr/bin/env python3
"""This the AirBnB console line interpreter"""

import cmd
import re
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class containing the entry point of the command interperter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command to exit the program."""
        exit()

    def do_EOF(self, arg):
        """Command to exit the program."""
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def help_create(self):
        """`create` command help"""
        print('Creates a new instance of BaseModel\n')

    def help_show(self):
        """`show` command help"""
        print('Shows a BaseModel instance if exists\n')

    def emptyline(self):
        """Nothing happens on empty entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            try:
                kclass = globals().get(arg, None)
                obj = kclass()
                obj.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Shows an instance given its id"""
        if not arg:
            print("** class name missing **")
            return
        strs = arg.split(" ")

        if not strs:
            print("** class name missing **")
            return

        kclass = globals().get(strs[0], None)
        if kclass is None:
            print("** class doesn't exist **")
            return

        if len(strs) != 2:
            print("** instance id missing **")
            return
        obj_id = "{}.{}".format(strs[0], strs[1])
        if obj_id in storage.all():
            print(storage.all()[obj_id])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance based on he class name and id"""
        if not arg:
            print("** class name missing**")
            return
        strs = arg.split(" ")
        count = len(strs)

        if count == 0:
            print("** class name missing**")
            return
        mName = strs[0]

        kclass = globals().get(mName, None)
        if kclass is None:
            print("** class doesn't exist **")
            return

        if count < 2:
            print("** instance id missing **")
            return

        obj_id = "{}.{}".format(strs[0], strs[1])

        if obj_id not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[obj_id]
        if obj.__class__.__name__ != mName:
            print("** no instance found **")
            return

        storage.all().pop(obj_id, None)
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        kclass = globals().get(arg, None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if v.__class__.__name__ != arg:
                continue
            print(v)

    def do_count(self, arg):
        """Print the count all class instances"""
        kclass = globals().get(arg, None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == arg:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update an instance base of class name and id"""
        if not arg:
            print("** class name missing **")
            return
        pattern = """^([A-Z][a-z]+)\s+([\w-]+)\s+([a-z_]+|\{[^}]+})(?:\s+("[^"]+"|\w+))?$"""

        m = re.match(pattern, arg)
        groups = [s for s in m.groups() if s] if m else []
        count = len(groups)

        if not groups:
            print("** class name missing **")
            return

        kclass = globals().get(groups[0], None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        mName = groups[0]

        if count < 2:
            print("** instance id missing **")
            return

        obj_id = "{}.{}".format(mName, groups[1])

        if obj_id not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[obj_id]
        if obj.__class__.__name__ != mName:
            print("** no instance found **")
            return

        if count == 3:
            """ dealing with a dictionary """
            if groups[2][0] != '{':
                print("** value missing **")
                return

            dictionary = json.loads(groups[2].replace("'", '"'))
            for key, value in dictionary.items():
                setattr(obj, key, value)
            return
        elif count < 3:
            print("** attribute name missing **")
            return

        attrName = groups[2]

        if count < 4:
            print("** value missing **")
            return

        attrValue = None
        try:
            attrValue = int(groups[3])
        except ValueError:
            pass

        if attrValue is None:
            try:
                attrValue = float(groups[3])
            except ValueError:
                pass

        if attrValue is None:
            attrValue = groups[3].replace('"', '')

        setattr(obj, attrName, attrValue)
        obj.save()

    def default(self, arg):
        if arg is None:
            return

        cmdPattern ="^([A-Z][a-z]+)\.([a-z]+)\(([^(]*)\)"
        paramsPattern = """^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?"""
        m = re.match(cmdPattern, arg)
        if not m:
            super().default()
            return
        mName, method, params = m.groups()
        m = re.match(paramsPattern, params)
        if m:
            params = [item for item in m.groups() if item]
        else:
            params = []
        #print(modelName)
        #print(method)
        #print(params)

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
