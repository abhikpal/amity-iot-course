# 
# MILESTONE 3
# 
# Simple login interface.
# 
# We continue with the problem described in the last milestone.
# 
# This program should ask the user for their name and print out a
# message if the name matches the intended user. If the names do not
# match, the program should print out an 'Access denied' message.
# 

username = 'Avi'

input_username = input("Enter your name to login: ")

if input_username == username:
    print("LOGIN SUCCESSFULL")
    print("You can now control your lights!")
else:
    print("ACCESS DENIED!")
