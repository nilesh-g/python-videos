
# Optional Parameters a.k.a. Default Arguments

def print_info(name, age, addr="Earth", email="Not Available"):
    print(f"Person Info: Name={name}, Age={age}, Addr={addr}, Email={email}")


print_info("James Bond", 65, "London", "james@bond.com") # Passed values are used for all arguments
print_info("James Bond", 65) # addr and email takes default values i.e. "Earth" and "Not Available"
