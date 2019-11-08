#!/usr/bin/python3
"""Define all attribute and methods for console"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_help(self):
        """Help command"""
        print("Help command for more information on existing commands")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
