#------------------------------------------------------------------------------------------------------------------
# Program name: Get_consent.py
# Program Author: Naomi Chen
# Date: 04/01/2020
# Last Amended: 04/01/2020
# Description: This program takes medical information from users and based on the answers 
# 			   gives the user their BMI. This program also gives commentary on their BMI
# 			   Also this program will keep customer information if they consent.
# Improvements: Save to csv, send to company email, build a web app. Deploy 
#
#------------------------------------------------------------------------------------------------------------------

"""
PSEUDOCODE get user consent 

declare a variable called answer and make it an empty string (Google search)


while ANSWER is not Y AND not N     (google while loop for two conditions)
print('Do you consent to sharing your information?')
get input from user as 'Y' or 'N' assign this to the variable ANSWER

---

if answer is no 
print'no problem! we will not save any of your data'
elseif answer is yes
print 'thank you! your data will help us improve our services'


"""
#------------------------------------------------------------------------------------------------------------------
#                     greet the user
#------------------------------------------------------------------------------------------------------------------
print('Welcome to the BMI test, you will be asked a series of questions to determine your BMI health score.')
print('')

#------------------------------------------------------------------------------------------------------------------
#                      GET USER CONSENT 
#------------------------------------------------------------------------------------------------------------------
answer = ''

while answer != 'Y' and answer != 'N':
	print('Do you consent to share your information?')
	answer = input('Y/N: ').upper()

print('')
if answer == 'Y':
	print('Thank you.You data will help us improve our services')
elif answer == 'N':
	print('Thank you. Your information will not be saved')
print('')


#------------------------------------------------------------------------------------------------------------------
#                 get the user name
#------------------------------------------------------------------------------------------------------------------
name = input('please input your name ')
full_name = str(name)
print ('Hello ' + full_name)


#------------------------------------------------------------------------------------------------------------------
#             get the user height
#------------------------------------------------------------------------------------------------------------------
while True:
	try:
		height =int(input('please input your height in cm: '))
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



#------------------------------------------------------------------------------------------------------------------
#           get the user weight
#------------------------------------------------------------------------------------------------------------------

while True:
	try:
		weight = int(input('Please input your weight in kg: '))
	except ValueError:
		print('Sorry try again')
	else:
		break

weight = int(weight)
print('your weight in kg is: ' + str("{:.2f}".format(weight)) + ' kg')
weight_in_stone = int(weight) * 0.15747304441777 
weight_in_stone = round(weight_in_stone, 2 )
print('your weight_in_stone is ' + str(weight_in_stone) + ' stone')



#------------------------------------------------------------------------------------------------------------------
#             BMI
#------------------------------------------------------------------------------------------------------------------
height_height = height * height
BMI = int(weight) / height_height
BMI =round(BMI, 2 )

print('')
print ('your BMI is: ' + str(BMI))

# REPORT BMI COMMENTARY 

if BMI < 18.50:
	print('You are in the underweight range')
elif 18.50 <= BMI <= 24.90:
	print('You are in the healthy weight range')
elif 25.00 <= BMI <= 29.90:
	print('You are in the overweight range')
elif 30.00 <= BMI <= 39.90:
	print('You are in the obese range')
else:
	print('You are extremely obese and at risk for serious health complications of obesity.')




#------------------------------------------------------------------------------------------------------------------
# generate report
#------------------------------------------------------------------------------------------------------------------
print('')
if answer == 'Y':
	print('Your data will be saved.')
elif answer =='N':
	print('Your data will not be saved.')
print('')
print('Thank you for taking the test.')	
