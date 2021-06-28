#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime
"""
Module consule.py a cmd console
"""


class HBNBCommand(cmd.Cmd):
    ''' a command interpreter class '''
    prompt = "(hbnb)"
    All_class_list = ["BaseModel", "User", "Place", "State",
                      "City", "Amenity", "Review"]

    @classmethod
    def get_objectsCount(self, clsname=""):
        ''' returns number of instnces created '''
        obj = storage.all()
        cnt = 0
        for key in obj.keys():
            obj_cls = (obj[key].__class__.__name__)
            if (obj_cls == clsname):
                cnt += 1
        return cnt

    def do_EOF(self, line):
        '''Quit command to exit the program'''
        return True

    def do_quit(self, line):
        ''' Quit command to exit the program '''
        return True

    def emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything '''
        pass

    def do_create(self, args):
        ''' Creates a new instance BaseModel, saves prints its id '''
        if args == "":
            print("** class name missing **")
        elif args not in HBNBCommand.All_class_list:
            print("** class doesn't exist **")
        else:
            new = eval(args)()
            print(new.id)
            new.save()

    def do_show(self, args):
        ''' Prints the string repr of an instances class name and id '''

        obj = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.All_class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            obj_key = (arg[0] + "." + arg[1])
            for key, value in storage.all().items():
                if key == obj_key:
                    print(value)
                    obj = 1
            if obj == 0:
                print("** no instance found **")

    def do_destroy(self, args):
        ''' Deletes an instance based on the class name and id (save changes
            into JSON file). Ex: $ destroy BaseModel 1234-1234-1234. '''

        obj = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.All_class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            obj_key = (arg[0] + "." + arg[1])
            objects = storage.all()
            for key, value in objects.items():
                if key == obj_key:
                    del objects[key]
                    obj = 1
                    storage.save()
                    storage.reload()
                    return
            if obj == 0:
                print("** no instance found **")

    def do_all(self, args):
        ''' Prints all string representation of all instances based or not
            on the class name. Ex: $ all BaseModel or $ all '''
        class_list = []
        if args == "":
            for key, value in storage.all().items():
                class_list.append(str(value))
            print(class_list)

        elif args in HBNBCommand.All_class_list:
            for key, value in storage.all().items():
                if args == key.split(".")[0]:
                    class_list.append(str(value))
            print(class_list)

        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        ''' Updates an instance based on the class name & id adding/updating
            attribute (save the change into the JSON file). Ex: $ update
            BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com". '''
        obj = 0
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.All_class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            obj_key = (arg[0] + "." + arg[1])
            for key, value in storage.all().items():
                if key == obj_key:
                    index = len(arg[0]) + len(arg[1]) + len(arg[2]) + 3
                    arg = args[index:]
                    if args[index] == "\"":
                        index += 1
                        arg = args[index:-1]
                    if hasattr(value, arg[2]):
                        arg = type(getattr(value, arg[2]))(args[index:])
                    setattr(value, arg[2], arg)
                    obj = 1
                    storage.save()
            if obj == 0:
                print("** no instance found **")
                return (-1)

    def default(self, args):
        ''' method defines actions on objects {<>}.all(), {<>}.count()
        {<>}.show(), {<>}.destroy(), {<>}.update()'''

        count = 0
        if len(args.split(".")) > 1:
            class_name = args.split(".")[0]
            if class_name in HBNBCommand.All_class_list:
                if args.split(".")[1] == "all()":
                    self.do_all(class_name)
                if args.split(".")[1] == "count()":
                    for key, value in storage.all().items():
                        if key.split(".")[0] == class_name:
                            count += 1
                    print(count)
                if args.split(".")[1].split("(")[0] == "show":
                    obj = args.split("\"")[1].split("\"")[0]
                    self.do_show(class_name + " " + obj)
                if args.split(".")[1].split("(")[0] == "destroy":
                    obj = args.split("\"")[1].split("\"")[0]
                    self.do_destroy(class_name + " " + obj)
                if args.split(".")[1].split("(")[0] == "update":
                    arg_list = args.split(".", 1)[1]
                    arg_list = arg_list.split("(")[1][:-1].split(",")
                    if "{" not in arg_list[1]:
                        obj = arg_list[0][1:-1]
                        name = arg_list[1][2:-1]
                        value = arg_list[2][1:]
                        if value[0] == "\"":
                            value = value[1:-1]
                        self.do_update(class_name + " " + obj +
                                       " " + name + " " + value)
                    else:
                        obj = arg_list[0][1:-1]
                        arg_dict = args.split(".")[1]
                        arg_dict = arg_dict.split("(")[1][:-1]
                        arg_dict = arg_dict.split("{")[1]
                        arg_dict = "{" + arg_dict
                        dict_ = eval(arg_dict)
                        for key, value in dict_.items():
                            ret = self.do_update(class_name + " " + obj +
                                                 " " + key + " " + str(value))
                            if ret == -1:
                                break
        else:
            cmd.Cmd.default(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
