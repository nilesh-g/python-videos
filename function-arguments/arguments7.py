
# Variable Length Arguments -- Positional

def function1(*args):
    print(f"args type: {type(args)}") # tuple
    print(f"first arg: {args[0]}")
    print(f"second arg: {args[1]}")
    print(f"third arg: {args[2]}")


function1("One", "Two", "three")
