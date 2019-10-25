import name_lib

# to import a library, be sure to use __name__ == __main__
if __name__ == "__main__":
    my_name = "Jimmy"
    upper_name = name_lib.upper_case_name(my_name)
    print(f"New name is: {upper_name}")

