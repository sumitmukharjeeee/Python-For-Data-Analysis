# Concatenation

name = "Michael Jackson"
print(name + "is the best")
print(3* "MJ ") 
name = name +"is the best"
print(name)
print("Michael Jackson is \t is best")
print("Michael Jackson is \n is best")
print("Michael Jackson is \\t is best")

print(r"Michael Jackson is \t is best") # r means raw string 

# String Methods

a = "Thriller is the sixth genre"
print(a.upper())
print(a.replace("Thriller","Comedy"))
print(a)

print(a.find("sixthsdf"))

# format strings

name = "Dua Lipa"
age = 35
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))

name  = "Jonathan"
age = 40

print("Ny name is %s and I am %d years old" %(name, age))