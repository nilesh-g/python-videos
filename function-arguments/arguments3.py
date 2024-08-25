
# Keyword Arguments

def print_info(name, age, addr, email):
    print(f"Person Info: Name={name}, Age={age}, Addr={addr}, Email={email}")


# print_info(name="James Bond", age=65, addr="London", email="james@bond.com") # Keyword args
print_info(age=65, email="james@bond.com", addr="London", name="James Bond") # Keyword args (may change sequence)
