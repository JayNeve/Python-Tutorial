l = [1,2,3,4,6,9]
cube = lambda x: x*x*x

# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)

#map()
newl = list(map(cube, l))
# print(newl)

#filter()
def filter_func(a):
    return a>=4
newlist = list(filter(filter_func,l))
# print(newlist)


#reduce()
from functools import reduce
def redu(a,b):
    return a+b
liste = reduce(redu, l)
print(liste)