
def outer_function():
    print("Inside the outer function")

    def inner_function():
        print("Inside the inner function")
    
    inner_function()


outer_function()


