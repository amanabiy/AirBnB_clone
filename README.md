# 0x00. AirBnB clone - The console
 Foundations > Higher-level programming > AirBnB clone

............................................................
............................................................
 
 
## First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called [ BaseModel ]) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB ([ User, State, City, Place… ]) that inherit from [ BaseModel ]
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash


## Tasks

## 0. README, AUTHORS  [ README.md, AUTHORS ]
  Write a README.md:
  * description of the project
  * description of the command interpreter:
  - how to start it
  - how to use it
  - examples
  * You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS)
  * You should use branches and pull requests on GitHub - it will help you as team to organize your work

## 1. Be PEP8 compliant!   [   ]

  Write beautiful code that passes the PEP8 checks. 

## 2. Unittests 
  All your files, classes, functions must be tested with unit tests
  > python3 -m unittest discover tests 
 **Warning:**

Unit tests must also pass in non-interactive mode:
  > echo "python3 -m unittest discover tests" | bash 
 
 
## 3. BaseModel  [  ]
  
  
  Write a class BaseModel that defines all common attributes/methods for other classes:
* [ models/base_model.py ]
* Public instance attributes:
   -- id: string - assign with an uuid when an instance is created:
   you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public instance attribute updated_at with the current datetime
to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class name of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel 

 you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The console

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)
%% an abstraction between “My object” and “How they are stored and persisted”

## Web static
* learn HTML/CSS
* create the HTML of your application
* create template of each object


## MySQL storage
* replace the file storage by a Database storage
* map your models to a table in database by using an O.R.M.

## Web framework - templating
* create your first web server in Python
* make your static HTML file dynamic by using objects stored in a file or database

## RESTful API
* expose all your objects stored via a JSON web interface
* manipulate your objects via a RESTful API 

## Web dynamic
* learn JQuery
* load objects from the client side by using your own RESTful API

## Files and Directories
* [ models ] directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* [ tests ] directory will contain all unit tests.
* [ console.py ] file is the entry point of our command interpreter.
* [ models/base_model.py ] file is the base class of all our models. It contains common elements:
- attributes: [ id, created_at and updated_at ]
- methods: [ save() and to_json() ]
- [ models/engine ] directory will contain all storage classes (using the same prototype). For the moment you will have only one: [ file_storage.py ].

## Storage
  Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.
  
## How can I store my instances?
  
  
## File storage == JSON serialization

- Convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method [ my_instance.to_json() ] 
to retrieve a dictionary
- convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a [ my_string = JSON.dumps(my_dict) ]
- write this string to a file on disk  

And the process of deserialization?
The same but in the other way:
- read a string from a file on disk
- convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a [ my_dict = JSON.loads(my_string) ]
- convert this data structure to instance - for us it will be a [ my_instance = MyObject(my_dict) ]

## *args, **kwargs

## datetime

## Data diagram
