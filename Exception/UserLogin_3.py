class AuthError(Exception):
    def __init__(self):
        print("User is disabled.")


demo_pass = "test"

c = 0
for i in range(3):
    user_inp = input("Enter password: ")
    try:
        if demo_pass == user_inp:
            print("Login successful")
        elif c == 2:
            raise AuthError
        else:
            print(f"Wrong password! {3-i-1} attempts left")
            c += 1
            
    except AuthError:
        print("No more attempts left.")