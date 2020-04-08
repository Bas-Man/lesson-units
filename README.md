# Package unit.Unit

This is a package to manage lesson units for both Students and Instructors.
It will be used to create calendars for both stake holders.

It consists of the following components:
- unit
- exceptions
- constants

### Todo:
add code and exceptions for checking string input on:
- material
- comment
- type
- location (optional?)

I am also consiering changing the __init__ method to just initalize the object.
I will define two different create methods, one the same as the current __init__
students and another for instructors, setting additional properities, bonus and
such. It might actually be worth subclassing student and instructor. But this
is just a proof of concept.
