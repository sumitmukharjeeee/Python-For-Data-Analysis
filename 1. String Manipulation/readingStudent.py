# import os
# print(os.getcwd())
with open("students.csv", "r") as f:
    lines = f.readlines()

print(lines)
print(lines[1].strip().split(","))