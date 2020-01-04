# this is my second program
# This program will get input on the users.
# This program will also convert their height

# Get user consent


# get the user name
name = raw_input('please input your name ')
full_name = str(name)
print ('Hello ' + full_name)



# get the user height
while True:
	try:
		height =int(raw_input('please input your height in cm:   '))
	except ValueError:
		print('Sorry try again')
	else:
		break
height = int(height) * 0.01
print('your height in m is: ' + str("{:.2f}".format(height)) + ' m')

# convert the user height
height_in_feet = height * 3.281
height_in_feet = round(height_in_feet, 2 )
print ('your height in feet is ' + str(height_in_feet) + ' feet ')

# get the user weight


while True:
	try:
		weight = int(raw_input('Please input your weight in kg:   '))
	except ValueError:
		print('Sorry try again')
	else:
		break

weight = int(weight)
print('your weight in kg is: ' + str("{:.2f}".format(weight)) + ' kg')
weight_in_stone = int(weight) * 0.15747304441777 
weight_in_stone = round(weight_in_stone, 2 )
print('your weight_in_stone is ' + str(weight_in_stone) + ' stone')




# BMI
height_height = height * height
BMI = int(weight) / height_height
BMI =round(BMI, 2 )

print('')
print ('your BMI is: ' + str(BMI))

"""
pseudocode error checking 

WHILE the condition is true (loop)
TRY and get the input 
if the input is wrong print 'input wrong try again'
ELSE BREAK the loop



PATTERN 

while:
	Try:

	Except:

	Else:
		break
"""

if BMI < 18.50:
	print'You are in the underweight range'
elif 18.50 <= BMI <= 24.90:
	print 'You are in the healthy weight range'
elif 25.00 <= BMI <= 29.90:
	print 'You are in the overweight range'
elif 30.00 <= BMI <= 39.90:
	print 'You are in the obese range'
else:
	print 'You are extremely obese and at risk for serious health complications of obesity.'


