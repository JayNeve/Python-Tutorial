# try:
#     a = int(input("Enter the number: "))
#     for i in range(1, 11):
#         print(f"{a} X {i} = {a*i}")
# except:
#     print("Invalid input")

# print("End of multiplication table")

try:
    a = int(input("Enter your age: "))
    print(f"You'r name is {a}")
except TypeError:
    print("Enter a valid age")
except ValueError:
    print("Enter a valid age")
finally:
    print("End of Code")

