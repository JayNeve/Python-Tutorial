dic = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(dic.get("john"))
print(dic.keys())
print(dic.values())
# print(dic.items())

for key, value in dic.items():
    print(key, value)