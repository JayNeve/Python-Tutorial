import math

class Calculator:
    def __init__(this, num):
        this.num = num
    def cube(this):
        cube = this.num*this.num*this.num
        print(f"Cube is {cube}")
    def square(this, num):
        this.num = num*num
        print(f"Square is {this.num}")
    def sqrt(this, num):
        this.num = math.sqrt(num)
        print(f"Square root is {this.num}")

obj = Calculator(16)
obj.cube()
obj.square(16)
obj.sqrt(16)