def outer_function():
    print("Inside outer function")

    def inner_function():
        print("Inside inner function")

    inner_function()

# Function call
outer_function()