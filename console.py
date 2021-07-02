#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from models.review import Review
from models.engine.file_storage import FileStorage

"""
Module consule.py a cmd console
"""


All_class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }


class HBNBCommand(cmd.Cmd):
    ''' a command interpreter class '''
    prompt = "(hbnb)"

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''Quit command CTRL+D to exit the program'''
        print("")
        return True

    def emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything '''
        pass

    def do_create(self, args):
        ''' Creates a new instance BaseModel, saves prints its id '''
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in All_class_dict:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        ''' Prints the string repr of an instances class name and id '''
        args = shlex.split(args)
        obj = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in All_class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) in obj:
            print(obj["{}.{}".format(args[0], args[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        ''' Deletes an instance based on the class name and id (save changes
            into JSON file). Ex: $ destroy BaseModel 1234-1234-1234. '''

        args = shlex.split(args)
        obj = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in All_class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) in obj:
            obj.pop("{}.{}".format(args[0], args[1]))
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        ''' Prints all string representation of all instances based or not
            on the class name. Ex: $ all BaseModel or $ all '''
        args = shlex.split(args)
        obj_dict = []
        my_dict = storage.all()
        if not args:
            for value in my_dict.values():
                obj_dict.append(str(value))
            print(obj_dict)
        elif args[0] in All_class_dict.keys():
            for k, v in my_dict.items():
                if v.__class__.__name__ == args[0]:
                    obj_dict.append(v.__str__())
            print(obj_dict)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        ''' Updates an instance based on the class name & id adding/updating
            attribute (save the change into the JSON file). Ex: $ update
            BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com". '''

        args = shlex.split(args)
        obj = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in All_class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif not "{}.{}".format(args[0], args[1]) in obj:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_key = obj["{}.{}".format(args[0], args[1])]
            setattr(obj_key, args[2], args[3])
            obj_key.save()

    def count(self, args):
        ''' counts number of instnces created '''
        arg = shlex.split(args, " ")
        obj = storage.all()
        cnt = 0
        if arg[0] not in All_class_dict.keys():
            print("** class doesn't exist **")
        for key, val in obj.items():
            if (arg[0] in key):
                cnt += 1
        print(cnt)

    def default(self, args):
        ''' default method for [<class>].show("") '''
        args = args.split(".")
        if len(args) > 1:
            if args[1] == 'all()':
                self.do_all(args[0])
            elif args[1] == 'count()':
                self.count(args[0])
            elif 'show' in args[1]:
                arg = args[1].split('"')
                self.do_show(args[0] + " " + arg[1])
            elif 'destroy' in args[1]:
                arg = args[1].split('"')
                self.do_destroy(args[0] + " " + arg[1])
            elif "update" in args[1]:
                arg = args[1].split('"')
                self.do_update(args[0] + " " + arg[1] + " " +
                               arg[3] + " " + arg[5])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
