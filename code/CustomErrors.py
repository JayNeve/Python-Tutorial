# a = int(input("Enter your age: "))

# if(a < 18 or a>65):
#     raise ValueError("Not Eligible to drive!!!")
# else:
#     print("Eligible to drive")


a = input("Enter a number between 1 and 10: ")

if(a.lower() == "quit"):
    exit()
elif(int(a) < 1 or int(a) > 10):
    raise ValueError("Number is not in the range of 1 to 10")
else:
    print(f"You entered {a}")