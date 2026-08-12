import os

folder = os.listdir("data")

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/day{i+1}")

print(os.getcwd())
os.chdir("D:")
print(os.getcwd())

# os.remove("./data")