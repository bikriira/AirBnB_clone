#!/usr/bin/python3
"""
This module serves as the command-line interface (CLI) entry point for
interacting with an AirBnB-like application

Usage:
- create <class_name>: Create a new instance of the specified class.

- show <class_name> <id> or <class_name>.show(<id>):
  Display details of the instance identified by the class name and ID.

- destroy <class_name> <id> or <class_name>.destroy(<id>):
  Remove the instance identified by the class name and ID.

- all <class_name> or <class_name>.all():
  List all instances of the specified class,
  but is no <class_name> print all available instances

- update <class_name> <id> <attribute_name> <attribute_value> or
  <class_name>.update(<id>, <attribute_name>, <attribute_value>):
  Update the attributes of an instance.

- quit/EOF: Exit the command interpreter.
"""

import ast
import datetime
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = "(hbnb)"

    def do_create(self, line):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id"""

        from models import storage
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in storage.active_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(inputs[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance,
           based on the class name and id"""

        from models import storage
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in storage.active_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif f"{inputs[0]}.{inputs[1]}" not in storage.objects:
            print("** no instance found **")
        else:
            obj = storage.objects[f"{inputs[0]}.{inputs[1]}"]
            print(str(obj))

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        from models import storage
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in storage.active_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif f"{inputs[0]}.{inputs[1]}" not in storage.objects:
            print("** no instance found **")
        else:
            del storage.objects[f"{inputs[0]}.{inputs[1]}"]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""

        from models import storage
        inputs = shlex.split(line)
        str_list = []
        class_name = inputs[0] if inputs else None

        if (class_name not in storage.active_classes) and class_name:
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if class_name is None:
                    str_list.append(str(obj))
                else:
                    if class_name == obj.__class__.__name__:
                        str_list.append(str(obj))
            print(str_list)

    def is_str_dict(self, str_):
        """Check if the passed string can be a dictionary"""

        try:
            return isinstance(ast.literal_eval(str_), dict)
        except (SyntaxError, ValueError):
            return False

    def do_update(self, line):
        """Updates an instance based on the class name and id,
           by adding or updating attribute
           (save the change into the JSON file)"""

        from models import storage
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in storage.active_classes:
            print(f"** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif f"{inputs[0]}.{inputs[1]}" not in storage.objects:
            print("** no instance found **")
        elif len(inputs) < 3:
            print("** attribute name missing **")
        elif self.is_str_dict(inputs[2]):
            inputs[2] = ast.literal_eval(inputs[2])
            obj = storage.objects[f"{inputs[0]}.{inputs[1]}"]

            for key, value in inputs[2].items():
                try:
                    curr_value = getattr(obj, key)
                    setattr(obj, key, type(curr_value)(value))
                except AttributeError:
                    setattr(obj, key, value)
            self.do_destroy(f"{inputs[0]} {obj.id}")
            storage.new(obj)
            obj.save()
        elif len(inputs) < 4:
            print("** value missing **")
        else:
            obj = storage.objects[f"{inputs[0]}.{inputs[1]}"]
            try:
                curr_value = getattr(obj, inputs[2])
                setattr(obj, inputs[2], type(curr_value)(inputs[3]))
            except AttributeError:
                setattr(obj, inputs[2], inputs[3])
            self.do_destroy(f"{inputs[0]} {obj.id}")
            storage.new(obj)
            obj.save()

    def precmd(self, line):
        """Play with user input before onecmd() even know """
        import re

        if line.endswith('.all()'):
            # Extract the class name
            class_name = line.split('.')[0]
            return f"all {class_name}"
        elif line.endswith(".count()"):
            class_name = line.split('.')[0]
            return f"count {class_name}"
        elif "." in line:
            line_chunks = line.split(".")
            match = re.search(r"(.(?<=\().*)", line)
            arg_tuple = ast.literal_eval(match.group(1))

            # If regex returns string resembling tuple with single value,
            # eval() sees it as string representation not tuple.
            # so we can simply use {arg_tuple} in that case

            if line_chunks[1].startswith("show("):
                return f"show {line_chunks[0]} {arg_tuple}"
            elif line_chunks[1].startswith("destroy("):
                return f"destroy {line_chunks[0]} {arg_tuple}"
            elif line_chunks[1].startswith("update("):
                # value can be inavailable if dictionary used
                value = "" if len(arg_tuple) < 3 else arg_tuple[2]
                return f"""update {line_chunks[0]}
                        {arg_tuple[0]} "{arg_tuple[1]}" {value}"""
        else:
            return line

    def do_count(self, line):
        """Counts all ocurence of class in the object stored"""
        from models import storage
        count = 0
        for key, obj in storage.objects.items():
            if (obj.__class__.__name__ == line):
                count += 1
        print(count)

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
