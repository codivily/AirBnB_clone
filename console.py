#!/usr/bin/env python3
"""This the AirBnB console line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class containing the entry point of the command interperter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        exit()

    def do_help(self, arg):
        print("Documented command (type help <topic>):")
        print("=======================================")
        print("EOF help quit")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
