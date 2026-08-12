# def average(a,b):
#     return (a + b) / 2
# print(average(b=5, a=3))

def avg(*num):
    '''This function takes any number of arguments and returns the average.'''
    sum =0
    for i in num:
        sum += i
    return sum / len(num)

print(avg(1, 2, 3, 4, 5))
print(avg.__doc__)