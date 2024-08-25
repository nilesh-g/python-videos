
# Variable Length Arguments -- Positional & Keyword

def function3(*args, **kwargs):
    print(f"args type: {type(args)} | kwargs type: {type(kwargs)}") # tuple | dict
    print(f"first arg: {args[0]}")
    print(f"second arg: {args[1]}")
    print(f"third arg: {kwargs['third']}")
    print(f"fourth arg: {kwargs['fourth']}")


function3("One", "Two", third="three", fourth="four")
