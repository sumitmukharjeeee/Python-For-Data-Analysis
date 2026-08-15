# # Concatenation

# name = "Michael Jackson"
# print(name + "is the best")
# print(3* "MJ ") 
# name = name +"is the best"
# print(name)
# print("Michael Jackson is \t is best")
# print("Michael Jackson is \n is best")
# print("Michael Jackson is \\t is best")

# print(r"Michael Jackson is \t is best") # r means raw string 

# # String Methods

# a = "Thriller is the sixth genre"
# print(a.upper())
# print(a.replace("Thriller","Comedy"))
# print(a)

# print(a.find("sixthsdf"))

# # format strings

# name = "Dua Lipa"
# age = 35
# print(f"My name is {name} and I am {age} years old")
# print("My name is {} and I am {} years old".format(name, age))

# name  = "Jonathan"
# age = 40

# print("Ny name is %s and I am %d years old" %(name, age))


names = ["Alice", "Elsaa","Nikita"]
loud_names = [n.upper() for n in names]
quiet_names = [n.lower() for n in names]
print(loud_names)
print(quiet_names)

scores = [85,78,91,29,12]
passing = [s for s in scores if s>=50]
print(passing, len(passing))

raw = "  Alice  "
print(raw.strip()) # removes leading/trailing whitespaces
print(raw.strip().lower())

line = "Alice, 85, 78, 91, 29, 12"
parts = line.split(",") # splits on comma into list of strngs
print(parts)

# the old way to do
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

# Comprehensive way

square = [x**2 for x in range(5)]
print(square)

words = [" data", "Analyst ", "PYTHON"]
cleaned = [w.strip().lower() for w in words]
print(cleaned)

