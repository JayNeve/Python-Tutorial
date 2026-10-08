class Person:
    def __init__(self, n, o):

        print("hey i'm a student")
        self.name = n
        self.occupation = o
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Jay", "Student")
b = Person("Chirag", "Gamer")

# print(a.name, a.age)
a.info()
b.info()