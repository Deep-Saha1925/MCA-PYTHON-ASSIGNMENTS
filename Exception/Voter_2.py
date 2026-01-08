age = int(input("Enter age: "))

try:
    if age >= 18:
        print("Valid for age")
    else:
        raise
except:
    print("You are underage.")