0x00. AirBnB clone - The console

This project aims to build an AirBnB replica using Python, HTML, CSS, Java,
APIs, database storage and Front-end integration.

The first Part is the building of the Console or command interpreter.
The work of this command line interpreter is to manage the objects of this
AirBnB project.

Functions of the line interpreter in this project
1. Creation of a new objects
2. Retrieving of an object from a file, database, etc...
3. Performing operations on objects e.g. count, compute stats, etc...
4. Updating attributes of an object
5. Destroying an object


Tasks
- put in place a parent class (called BaseModel) to take care of the
initialization, serialization and deserialization of your future instances

- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

- create the first abstracted storage engine of the project: File storage.

- create all unittests to validate all our classes and storage engine
