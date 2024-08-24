
def create_greeter():
    def greet(name):
        print("Hello, " + name + "!")
    return greet


say_hello = create_greeter()
say_hello("Nilesh")
