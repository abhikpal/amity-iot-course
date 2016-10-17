# 
# MILESTONE 3
# 
# Simple login interface.
# 
# Avi wants to control the lights in his room through the internet when
# he is away from home. This system will be online and we need a login
# interface that will give Avi access to the light in his room. We also
# want to prevent other people from interfering with Avi's lights.
# 
# This program should ask the user for their name and print out a
# message if the name matches the intended user.
# 

username = 'Avi'

input_username = input("Enter your name to login: ")

if input_username == username:
    print("LOGIN SUCCESSFULL")
    print("You can now control your lights!")
