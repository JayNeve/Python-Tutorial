a = int(input("Enter your age: "))

match a:
    case a if a >= 18 and a <= 75:
        print("You are eligible to drive.")
    case _:
        print("You are not eligible to drive.")