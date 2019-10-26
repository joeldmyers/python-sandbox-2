import os, sys

my_folder = os.getcwd()

print(f"Here are the files in {my_folder}")

# 'with' is a context manager that helps deal with cleanup.

# the below will list all the files in the current folder.
with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f" - { entry.name }")


# sys.  Going to take 

arguments = sys.argv

print(arguments)