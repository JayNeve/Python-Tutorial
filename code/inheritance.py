class Employee:
    def __init__(this, name, id):
        this.name = name
        this.id = id
    def showDetails(this):
        print(f"The name of employee is {this.name} and his id is {this.id}")

class Programmer(Employee):
    def showLang(this):
        print("The default language is Python")

e = Employee("Jay Neve", 5)
e.showDetails()