# this is my second program
# This program will get input on the users.
# This program will also convert their height

# get the user name
name = raw_input('please input your name ')
full_name = str(name)
print ('Hello ' + full_name)

# get the user height
height = raw_input('please input your height in cm: ')
height = int(height) * 0.01

print('your height in m is: ' + str(height) + 'm')

# print(str(height) + 'm')


# convert the user height
height_in_feet = height * 3.281
height_in_feet = round(height_in_feet, 2 )
print ('your height in feet is ' + str(height_in_feet) + ' feet ')
