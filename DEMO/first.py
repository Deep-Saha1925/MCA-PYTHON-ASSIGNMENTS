def gcd(a, b):
    while b != 0:
        a = b
        b = a % b
        
    return a

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function call
result = gcd(num1, num2)
print("GCD =", result)