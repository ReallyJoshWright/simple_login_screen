# Simple Login Screen

This is a PyQt6 login screen that allows a to create a login that gets stored 
in a postgresql database using bcrypt to hash and salt the user's password. 
This program utilizes a makefile to give options to create an executable file.

## Instructions
- run make to generate an executable that uses the python interpreter
- run make clean to remove extraneous files and directories
- run make exe to generate an actual executable

## Progress (Todo)
- Add code to check username availability
- Clean up design
- Create tests
- Handle the case when a user closes the dialog and it shows that the user has
    logged in
