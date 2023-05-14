# AirBnB clone - the console for alx projcet
============================================

 By: Shakir Muhammedsaid, Kelvin AGIMOGIM

## Description
  - The console: It is an interactive shell that enables testing of the given classes in interactive and non-interactive mode. It is help full for debbuging and development. It has features to create new instance, show the info of an instance, update an attribute of an instance, destroy an instance, all instance of the specified class.
  - Class Structure: it Uses BaseModel class as the base for all other classes with attributes of ```id```, ```created_at``` and ```updated_at```.
    - BaseModel
      - User
      - State
      - City
      - Amenity
      - Place
      - Review
  - Storage Engine: as storage it uses json file to save the instances and has built-in serializing and deserializing features.
  ```<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>```.
  - Testing: testing is performed using unittest. All testing files are found in ```tests/``` folder. ```python3 -m unittest discover tests``` command can be used to run all tests.
### Available classes

### Usage
  - clone this repo and run it using "./console.py" to open the console
  - ```help``` provides help for each command
  - ```quit``` or ```EOF``` to exit the console
  - ```create <class name>``` or to create a new instance of a class. eg. ```create User```
  - ```show <class name> <instance_id>``` or ```<class name>.show(<id>)``` prints the contents of the instance with the given id in the specified class
  - ```count <class name>``` or ```<class name>.count()```counts the number of instances that belongs to the specified class
  - ```destroy <class name> <instance_id>``` or ```<class name>.destroy(<id>)```deletes the instance of the given class with the given id
  - ```all``` prints every instance of any class that was created
  - ```all <class name>``` or ```<class name>.all()``` prints every instance that belongs to the given class name
  - ```update <class name> <id> <attribute name> "<attribute value>"``` or ```<class name>.update(<id>, <attribute name>, <attribute value>)```it updates an attribute of an instance of the given class with the given id
  - ```<class name>.update(<id>, <dictionary representation>)``` to update the instance with the specified id using dictionary```
### Examples
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help show
Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.

(hbnb)
(hbnb) create User
ea561ba2-3824-4ca4-8f72-6a725bb47a27
(hbnb) create User
e6285882-1cb1-4537-ae85-a97a95933271
(hbnb) create State
a4b36f01-7e14-416e-a685-09acff246a06
(hbnb)
(hbnb) User.count()
2
(hbnb) State.count()
1
(hbnb)
(hbnb) all
["[User] (ea561ba2-3824-4ca4-8f72-6a725bb47a27) {'id': 'ea561ba2-3824-4ca4-8f72-6a725bb47a27', 'created_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456121), 'updated_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456124)}", "[User] (e6285882-1cb1-4537-ae85-a97a95933271) {'id': 'e6285882-1cb1-4537-ae85-a97a95933271', 'created_at': datetime.datetime(2023, 5, 14, 21, 24, 44, 591515), 'updated_at': datetime.datetime(2023, 5, 14, 21, 24, 44, 591520)}", "[State] (a4b36f01-7e14-416e-a685-09acff246a06) {'id': 'a4b36f01-7e14-416e-a685-09acff246a06', 'created_at': datetime.datetime(2023, 5, 14, 21, 24, 52, 373675), 'updated_at': datetime.datetime(2023, 5, 14, 21, 24, 52, 373678)}"]
(hbnb) all User
["[User] (ea561ba2-3824-4ca4-8f72-6a725bb47a27) {'id': 'ea561ba2-3824-4ca4-8f72-6a725bb47a27', 'created_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456121), 'updated_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456124)}", "[User] (e6285882-1cb1-4537-ae85-a97a95933271) {'id': 'e6285882-1cb1-4537-ae85-a97a95933271', 'created_at': datetime.datetime(2023, 5, 14, 21, 24, 44, 591515), 'updated_at': datetime.datetime(2023, 5, 14, 21, 24, 44, 591520)}"]
(hbnb)
(hbnb) destroy State a4b36f01-7e14-416e-a685-09acff246a06
(hbnb) count State
0
(hbnb)
(hbnb) show User ea561ba2-3824-4ca4-8f72-6a725bb47a27
[User] (ea561ba2-3824-4ca4-8f72-6a725bb47a27) {'id': 'ea561ba2-3824-4ca4-8f72-6a725bb47a27', 'created_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456121), 'updated_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456124)}
(hbnb) User.show(ea561ba2-3824-4ca4-8f72-6a725bb47a27)
[User] (ea561ba2-3824-4ca4-8f72-6a725bb47a27) {'id': 'ea561ba2-3824-4ca4-8f72-6a725bb47a27', 'created_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456121), 'updated_at': datetime.datetime(2023, 5, 14, 21, 24, 43, 456124)}
(hbnb)
(hbnb) EOF
```
