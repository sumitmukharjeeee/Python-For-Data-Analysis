# # Errors are big issues comingfrom sustem on the 
# # other hand exceptions can be controlled
# # Zerodivision error
# result = 10/0
# print(result)

# # value error
# num = int("abc")

# # file not found error
# with open("nonexi.txt","r") as file:
#     content = file.read()

# Handling exception

# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Error:Cant divide by zero")

# print("Outside try and except block")

# Multiple exceptionsa t once

# try:
#     value = int('abc')
# except (ValueError, TypeError):
#     print("Something in the way")

# else and finally

# try:
#     file = open("data.csv")
# except FileNotFoundError:
#             print("file not found")
# else:
#         print("file opened ")
#         file.close()
# finally:
#         print("This runs no mater what")    

# a = 1
# try:
#     b = int(input("Please enter a number to divide a: "))
#     a = a / b
#     print("Success a =", a)
# except:
#     print("There was an error")


try:
    # Attempting to divide by 10
    result = 10/0
except ZeroDivisionError:
    # Handling and printing zwro error msg
    print("Eroor cant divide")
# This line will be executed regarledd of expection
print("outside of try and except")


