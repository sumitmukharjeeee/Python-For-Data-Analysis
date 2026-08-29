# create a new file for writing

# with open("file2.txt", 'w') as file:
#     file2.write("This is live")
#     file2.write("this is a line")
    # file 1 ia auto closed when with block exits


# writing multilel lines to a file using  alist and loop

# Lines = ["This is line 1", "this is line 2","this is line 3"]

# with open("Example3.txt",'w') as file2:
#     for line in Lines:
#         file2.write(line+'\n')


# Appending data to existing files

new_data = "This is line C"

with open("Examples2.txt","a") as file2:
    file2.write(new_data+'\n')