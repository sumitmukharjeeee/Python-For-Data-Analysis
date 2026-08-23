set1 = {"pop","rock","sock","rock"}

print(set1)

list1 = [1,2,3,1,3,4,5,6]
print(set(list1))

# set operations

A = {"Thriller", "Back in Black","AC/DC"}
A.add("CAS")
print(A)
print(A.remove("Thriller"))
# print(A.remove(""))

# Intersection
B = {"Thriller", "Chainsmokers","Paris","AC/DC"}

print(A&B)
# Union
print(A.union(B))
