class AuthError(Exception):
    def __init__(self):
        print("User is disabled.")


demo_pass = "test"

for i in range(3):
    user_inp = input("Enter password: ")
    try:
        if demo_pass == user_inp:
            print("Login successful")
        elif i != 2:
            print(f"Wrong password! {3-i-1} attempts left")
        else:
            raise AuthError
            
    except AuthError:
        print("No more attempts left.")