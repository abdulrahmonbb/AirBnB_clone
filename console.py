#!/usr/bin/python3

"""
This script contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Represents the class for the command interpreter.
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        print()
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()