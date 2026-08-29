with open("C:\Users\Sumit Mukharjee\Downloads\Python-For-Data-Analysis\8.reading files\sample.txt","r") as file:
    file_stuff = file.read()

    print(file_stuff)
# It returns a file object, which is stored in the variable file. The 'r' mode indicates that the file will be opened for reading

# with open('file1.txt','r') as file:
    # further code it auto close


# reading the content line bu line
file  = open('file.txt', 'r')

# read first line
line1 = file.readline()
# read second lone 
line2 = file.readline()