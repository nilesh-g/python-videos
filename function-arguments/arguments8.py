
# Variable Length Arguments -- Keyword

def function2(**kwargs):
    print(f"kwargs type: {type(kwargs)}") # dict
    print(f"first arg: {kwargs['first']}")
    print(f"second arg: {kwargs['second']}")
    print(f"third arg: {kwargs['third']}")


function2(first="One", second="Two", third="three")
