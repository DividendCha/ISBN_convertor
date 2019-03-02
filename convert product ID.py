import math
import string
cont = 'Y'
while cont=='Y':
	
	productID = ""
	print "Please key-in the Product ID and press enter for generate ISBN:-"
	check1 = raw_input()
	try:
		check2 = int(check1)
		productID = str(check1)
		tempPID = productID[3:]
		result = 0
		temp = 0.0
		times = 10
		finalResult = 'X'

		for a in tempPID:
			temp =(int(a)*times) + temp
			times -= 1
		 
		result = int(math.ceil(temp/11)*11 - temp)
		if result > 9:
			tempPID = tempPID + finalResult
		else:
			tempPID = tempPID + str(result)
		print "ISBN: " , tempPID
		print "" 
		cont = raw_input("Continue(Y/N):").upper()

	except ValueError:
		cont = raw_input("Invalid Input, Continue(Y/N):").upper()
		print ""