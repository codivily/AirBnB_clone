#!/usr/bin/env python3
"""This the AirBnB console line interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class containing the entry point of the command interperter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        exit()

    def do_help(self, arg):
        if arg == 'quit':
            print('Quit command to exit the program')
        else:
            print("Documented command (type help <topic>):")
            print("=======================================")
            print("EOF help quit")

    def do_create(self, arg):
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
        if not arg:
            print("** class name missing **")
            return
        strs = arg.split(" ")

        if not strs:
            print("** class name missing **")
            return

        constructor = globals().get(strs[0], None)
        if constructor is None:
            print("** class doesn't exists **") 
            return

        if len(strs) != 2:
           print("** instance id missing **")
           return
       
        if strs[1] in storage.all():
           print(storage.all()[strs[1]])
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
