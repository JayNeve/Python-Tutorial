import random 

def game(user, comp):
    if(user == comp):
        print("Match Draw!")
    elif(user==1 and comp==2):
        print("user won!")
    elif(user==2 and comp==3):
        print("user won!")
    elif((user==3 and comp==1)):
        print("user won!")
    elif((user==1 and comp==3)):
        print("computer won!")
    else:
        print("computer won!")
user = int(input("Enter 1 for snake, 2 for water, 3 for gun: "))
comp = random.randint(1,3)

print(f"user gave {user} computer said {comp}")


game(user, comp)