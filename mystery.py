def mystery():
    num = 10 * 3
    
    if num == 10:
        num = num * 10
    elif num == 30:
        num = num * 30

    return f"The number here is {num}"

print(mystery())
