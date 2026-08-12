a = [30, 24, 45, 56, 24, 90, 23]
for index, mark in enumerate(a):
    # print(mark)
    if(index == 5):
        print(f"The marks of jay is {mark}")

pair_mark = [f"{i}, {item}" for i, item in enumerate(a, start=1)]

print(pair_mark)