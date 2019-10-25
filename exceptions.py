# exceptions testing
# This will throw an error
try:
    int("a")

except ValueError as e:
    print(f"A didn't work: {e}")

print("this is the end of my program")