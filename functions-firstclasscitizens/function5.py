
def add(x, y):
    return x + y

def apply_operation(x, y, operation):
    return operation(x, y)


result = apply_operation(5, 3, add)
print("add :", result)
