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
# better at memory allocation because it doesn't contain the entire list in memory, it only handles the current one
# and goes on to the next one. 

# Just like a list comprehension, set comprehension, but with parentheses
names=["Jim", "Jam", "Jom"]
(len(name) for name in names)



# Slicing

my_string = "Hello, World"

my_string[0] # = "H"
my_string[-1] # = "!"

# This can take a second parameter.  

print(my_string[0:5]) # Hello


# also the 0 is optional

my_string[:5]

# with lists, we can do the same. 

# When you say new variable assigned to existing array, it's by reference and doesnt create 

new_names = names

# now we have two pointers to the same array

# so a nice trick to copy is - 

newer_names = names[:]

# to reverse an array: 
my_list = list(range(10))
print(my_list[::-1])



# Zipping

# let's create a dictionary

squares = {num: num * num for num in range(11)}

print(squares)

print(squares.keys())
print(squares.values())

print(squares.items())
# This last one gives us a list of tuples.

# We can go the other way, combining two lists to make a zip object

players = ["Jane", "John", "Jorge"]
scores = [100, 5, 50]

zip(players, scores)

# use unpacking then
for name, score in zip(players, scores):
    print(f"{name} had a score of {score}")

# we can use a comprehension also

[print(f"Mr. {name} had a score of {score}") for name, score in zip(players, scores)]