# simple example of importing a library
def upper_case_name(name):
    return name.upper()


# This is best practice for creating a library. This will only run if we are running this file directly
# Otherwise, when imported, it will not run
if __name__ == "__main__":
    name = "Joel"
    new_name = upper_case_name(name)
    print(new_name)