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

# We can do this conditionally as well

times_five_squares = [num * num for num in range(100) if num % 5 == 0]

print(times_five_squares)


lottery_num_string = "4, 5, 134, 10"

# to get the max do this 

hi_num = max(int(num) for num in lottery_num_string.split(', '))

print(f"The high number is {hi_num}")

# Doing set comprehension: 

# to make a set:

set_one = { num * num for num in range(10)}
print(set_one)

# to make a dictionary: 

dictionary_one = {num: num * num for num in range(100)}
print(dictionary_one)
print(dictionary_one[10])


# Generators!  
# better at memory allocation

# TODO - go back and look at the generator expressions.