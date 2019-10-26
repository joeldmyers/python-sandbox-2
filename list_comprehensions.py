# List Comprehensions

names = ["Jane", "Molly", "Cameron"]

# make upper case

upper_names = []
for name in names:
    upper_case_name = name.upper()
    upper_names.append(upper_case_name)

print(upper_names)

# to do list comprehension: 

print([name.upper() for name in names])

# Range example

squares = [num * num for num in range(50)]

print(squares)

# So it's [ OPERATION TO RETURN for item in iterable]