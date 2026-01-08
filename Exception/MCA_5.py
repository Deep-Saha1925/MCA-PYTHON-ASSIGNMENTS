class NotEligible(Exception):
    def __init__(self, msg):
        print(msg)

ug_marks = int(input("Enter percentage marks in UG: "))
jeca_rank = int(input("Enter jeca rank(if not give -1): "))
maths = input("Enter (Y) for maths in HS or UG else (N): ")
reserved = input("Reserved? (Y/N)")

try:
    if maths == "Y":
        if reserved == "Y":
            if ug_marks >= 45:
                print("Eligible.")
            else:
                raise NotEligible("Marks should be more than 45% for reserved.")
        elif reserved == "N":
            if ug_marks >= 50:
                print("Eligible.")
            else:
                raise NotEligible("Marks should be more than 50% for unreserved.")
    else:
        raise NotEligible("You should have maths in HS or UG")
        
except NotEligible:
    print("Not eligible for MCA")