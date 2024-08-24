def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = [add, subtract]


for op in operations:
    result = op(5, 3)
    print(op.__name__, "result :", result)
