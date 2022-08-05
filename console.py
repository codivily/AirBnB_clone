#!/usr/bin/env python3
"""This the AirBnB console line interpreter"""

import cmd
from models.base_model import BaseModel
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
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            try:
                constructor = globals().get(arg, None)
                obj = constructor()
                obj.save()
                print(obj.id)
            except:
                print ("** class doesn't exist **")
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
       
        if strs[1] in storage.all():
           print(storage.all()[strs[1]])
        else:
            print("** no instance found **")
    
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

    def do_update(self, arg):
        """Update an instance base of class name and id"""
        if not arg:
            print("** class name missing **")
            return
        strs = arg.split(" ")
        count = len(strs)
        if not strs:
            print("** class name missing **")
            return
        
        kclass = globals().get(strs[0], None)
        if kclass is None:
            print ("** class doesn't exist **")
            return
        className = strs[0]

        if count < 2:
            print("** instance id missing **")
            return
        objId = strs[1]

        if  objId not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[objId]

        if count < 3:
            print("** attribute name missing **")
            return
        attr_name = strs[2]

        if count < 4:
            print("** value missing **")
            return
        attr_value = strs[3]

        if hasattr(obj, attr_name):
            setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_value))
        else:
            setattr(obj, attr_name, attr_value)

        obj.save()

        





if __name__ == '__main__':
    HBNBCommand().cmdloop()
