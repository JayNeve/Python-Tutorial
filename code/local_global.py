a = 4
# print(a)

def local():
    global a
    a = 5
    print(f"This is a local variable", a)

print(f"This is a global variable", a)
local()
print(f"This is a global variable", a)
