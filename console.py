#!/usr/bin/python3
import datetime
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
"""contains the entry point of the command interpreter"""


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
            obj_dict_repr = storage.objects[f"{inputs[0]}.{inputs[1]}"]
            obj = eval(inputs[0])(**obj_dict_repr)
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
        class_name = inputs[0] if inputs else "BaseModel"

        if class_name not in storage.active_classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                obj = eval(inputs[0])(**value)
                str_list.append(str(obj))
            print(str_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id,
           by adding or updating attribute
           (save the change into the JSON file)"""

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
        elif len(inputs) < 3:
            print("** attribute name missing **")
        elif len(inputs) < 4:
            print("** value missing **")
        else:
            obj_dict_repr = storage.objects[f"{inputs[0]}.{inputs[1]}"]
            obj = eval(inputs[0])(**obj_dict_repr)
            try:
                curr_value = getattr(obj, f"{inputs[2]}")
                setattr(obj, f"{inputs[2]}", type(curr_value)(inputs[3]))
            except AttributeError:
                setattr(obj, f"{inputs[2]}", inputs[3])
            self.do_destroy(f"{inputs[0]} {obj.id}")
            storage.new(obj)
            obj.save()

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
