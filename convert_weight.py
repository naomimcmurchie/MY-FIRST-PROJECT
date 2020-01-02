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
#print('your height in m is: ' + str(height) + ' m')
print('your height in m is: ' + str("{:.2f}".format(height)) + ' m')
#{:.2f}".format())


# convert the user height
height_in_feet = height * 3.281
height_in_feet = round(height_in_feet, 2 )
print ('your height in feet is ' + str(height_in_feet) + ' feet ')


# get the user weight
weight = raw_input('please input your weight in kg: ')
print('your wight in kg is: ' + str(weight) + ' kg')

weight_in_stone = int(weight) * 0.15747304441777 
weight_in_stone = round(weight_in_stone, 2 )
print('your weight_in_stone is ' + str(weight_in_stone) + ' stone')


# BMI
height_height = height * height
BMI = int(weight) / height_height

print ('your BMI is: ' + str(BMI))
