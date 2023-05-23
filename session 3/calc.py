import platform

f1 = open("CalcHistory.txt", "a+") 
while(True):
	num1 = int(input("enter first opernad"))
	num2 = int(input("enter second operand"))

	op = input("enter the operation")

	if (op == '+'):
		print("%d + %d = %d "%(num1,num2,num1+num2) )
		f1.write("%d + %d = %d "%(num1,num2,num1+num2) )
	elif (op == '-'):
		print("%d - %d = %d "%(num1,num2,num1-num2) )
		f1.write("%d - %d = %d "%(num1,num2,num1-num2) )
	elif (op == '*'):
		print("%d * %d = %d "%(num1,num2,num1*num2) )
		f1.write("%d * %d = %d "%(num1,num2,num1*num2) )
	elif (op == '/'):
		print("%d / %d = %d "%(num1,num2,num1/num2) )
		("%d / %d = %d "%(num1,num2,num1/num2) )
		f1.write
	else:
		print("undefined input")