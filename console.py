#!/usr/bin/python3
import cmd
"""contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb)"

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
