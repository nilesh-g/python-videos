
# Position-only Arguments

def print_info(name, age, addr, email, /):
    print(f"Person Info: Name={name}, Age={age}, Addr={addr}, Email={email}")


print_info("James Bond", 65, "London", "james@bond.com") # Positional args -- Okay
# print_info(name="James Bond", age=65, addr="London", email="james@bond.com") # Keyword args -- Error
