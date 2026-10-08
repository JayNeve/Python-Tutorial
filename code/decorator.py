def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello World")
        fx(*args, **kwargs)
        print("thank for using the func")
    return mfx

@greet
def add(a, b):
    print(a+b)

add(1, 2)