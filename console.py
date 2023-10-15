#!/usr/bin/python3
import cmd

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, "Place": Place
           ,"Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    prompt = '(hnhb)'

    def do_quit(self, arg):
        """Exits CLI

        @rtype: object
        """
        print()
        return True

    def do_eof(self, arg):
        """Exits CLI

        @rtype: object
        """
        return True

    def do_create(self, args):

        arg = args.split()

        if len(arg) <= 0:
            print('** class name missing **')

        if arg in classes:
            for key, value in classes.items():
                if arg[0] == key:
                    new_instance = value()
                    print(new_instance.id)
                    new_instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """prints the string representation of an instance
           based on the class name and id"""
        arg = args.split()
        new_dict = storage.all()
        if len(arg) <= 0:
            print('** class name missing **')
        elif len(arg) != 2:
            print('** instance id missing **')
        elif len(arg) in classes:
            if arg[0]+"."+arg[1] in new_dict:
                print(new_dict[arg[0] + "." + arg[1]])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """destroys the instance
        based on the class name and id"""
        arg = args.split()
        new_dict = storage.all()
        if len(arg) <= 0:
            print('** class name missing **')
        elif len(arg) != 2:
            print('** instance id missing **')
        elif arg in classes:
            if arg[0] + "." + arg[1] in new_dict:
                new_dict().pop(arg[0] + "." + arg[1])
                storage.save(new_dict)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):

        arg = args.split
        new_dict = storage.all()
        all_instance = []
        if arg in classes:
            if arg[0] + "." + arg[1] in new_dict:
                print(new_dict[arg[0] + "." + arg[1]])
        elif len(args) == 0:
            for key in new_dict:
                all_instance.append(new_dict[key].__str__())
            print(all_instance)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):

        arg = args.split
        new_dict = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif arg[0] + "." + arg[1] not in new_dict:
            print("** no instance found **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            k = arg[0] + "." + arg[1]
            attr = arg[2]
            v = arg[3].replace('"', ' ')
            instance = new_dict[k]
            if hasattr(instance, attr) and type(getattr(instance, attr)) is int:
                if v.isnumeric():
                    v = int(v)
            elif hasattr(instance, attr) and type(getattr(instance, attr)) is float:
                idk = args[3].split(".")
                if idk[0].isnumeric() and idk[1].isnumeric():
                    v = float(v)
            setattr(storage.all()[k], attr, v)
            storage.all()[k].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()