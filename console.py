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
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[args[0] + "." + args[1]])

    def do_destroy(self, line):
        """Destroy command to delete instance
        """
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()

    def do_all(self, line):
        """All command to print all string representation or specified class
        """
        if line == "":
            for v in storage.all().values():
                print([str(v)])
        elif line in classes:
            for k, v in storage.all().items():
                key = k.split(".")
                if key[0] == line:
                    print([str(v)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update command to update instance attribute and saves
        """
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            args = args[0:4]
            k = args[0] + "." + args[1]
            instance = storage.all()[k]
            args[3] = eval(args[3])
            setattr(instance, args[2], args[3])
            instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
