#!/usr/bin/python3
"""Define all attribute and methods for console"""
import cmd
from models import storage, classes


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def help_help(self):
        """Help command"""
        print("Help command for more information on existing commands\n")

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create command to create new instance and save
        """
        if line == "":
            print("** class name missing **")
        elif line in classes:
            new_model = classes[line]()
            new_model.save()
            print(new_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show command to print string representation of instance
        """
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
