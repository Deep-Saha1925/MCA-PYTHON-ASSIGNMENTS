x = 10  # global variable

def outer():
    y = 20  # enclosing variable

    def inner():
        global x
        nonlocal y
        x = x + 5
        y = y + 5
        print("Inside inner function")
        print("Global x:", x)
        print("Nonlocal y:", y)

    inner()

outer()
print("Outside function, Global x:", x)