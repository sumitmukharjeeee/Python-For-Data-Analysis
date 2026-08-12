# tuples are ordered sequence

list1 = [1,2,3,4]
print(list1)
list1.append(5)
print(list1)
list2 = [1,2,3,4,5,6,6]
new_list = list2.copy() 
print(new_list)
print(new_list.count(3)) # no of occurences count)

del new_list[2]
print(new_list)

list3 = [6,7,8]
list3_extend = [9,10]
list3.extend(list3_extend)
print(list3)