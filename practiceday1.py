# Var and Types
name = "Sumit Mukharjee"
years_of_experience = 5
gpa = 7.98
isReady = True

#Lists and Dicts - very imp for data 
scores = [10, 20, 30, 40, 50]
student = {"name":"Ravi", "scores":[10, 20, 30, 40, 50]}

# Loops
for s in scores:
    print(s)

# Functiions
def average(nums):
    return sum(nums)/len(nums)
print(average(scores))

x = [10,20]
x.append(30)
print(x[1], x[-1])

d = {"a":1, "b":2}
d["c"] = 3
print(len(d))
print(d)