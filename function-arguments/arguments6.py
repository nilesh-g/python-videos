
# Position-only + Keyword-only Arguments

def print_info(name, age, /, *, addr, email):
    print(f"Person Info: Name={name}, Age={age}, Addr={addr}, Email={email}")


print_info("James Bond", 65, addr="London", email="james@bond.com") # First two Positional and Next two Keyword -- Okay
# print_info(name="James Bond", age=65, addr="London", email="james@bond.com") # Keyword only args -- Error
# print_info("James Bond", 65, "London", "james@bond.com") # Positional only args -- Error
