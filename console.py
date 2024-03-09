#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
"""contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_create(self, line):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id"""
        inputs = shlex.split(line)
        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)            

    def do_show(self, line):
        from models import storage

        inputs = shlex.split(line)
        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif f"{inputs[0]}.{inputs[1]}" not in storage.__objects:
            print("** no instance found **")
        else:
            print(storage.__objects[f"{inputs[0]}.{inputs[1]}"])

    def emptyline(self):
        """Handle an empty line input"""
        pass

    def do_EOF(self, line):
        """Usually Ctrl+D on Unix-like systems and Ctrl+Z on Windows"""
        return True

    def do_quit(self, line):
        """Usually Ctrl+D on Unix-like systems and Ctrl+Z on Windows"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
