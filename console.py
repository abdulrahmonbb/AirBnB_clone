#!/usr/bin/python3

"""
This script contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Represents the class for the command interpreter.
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        args = line.split()
        if not line:
            print([str(v) for v in storage.all().values()])
        elif args[0] in storage.classes():
            print([str(v) for k, v in storage.all().items() if args[0] in k])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on class name and id by adding or updating an attribute.
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()