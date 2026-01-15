def show_details(**kwargs):
    print("Details received:")
    for key, value in kwargs.items():
        print(key, ":", value)

# Function calls
show_details(name="Deep", age=22)
show_details(course="MCA", university="MAKAUT", year=2025)