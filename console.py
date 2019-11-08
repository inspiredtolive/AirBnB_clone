#!/usr/bin/python3
"""Define all attribute and methods for console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
