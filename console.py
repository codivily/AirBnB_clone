#!/usr/bin/env python3
"""This the AirBnB console line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class containing the entry point of the command interperter"""
    prompt = "(hbnb) "

    doc_header = 'Documented commands (type help <topic>):'

    def do_quit(self, arg):
        """Command to exit the program."""
        exit()

    def help_quit(self):
        print('Quit command to exit the program')

    def do_EOF(self, arg):
        """Command to exit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
