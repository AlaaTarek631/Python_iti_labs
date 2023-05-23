#collect the list
y =input("enter 4 numbers separated with & sign").split("&",4)
#initialte the list values
list = y
#prit them to check
print (y)
#ask for the number to search
x = input("enter the number you need to search")
#search the number through the list
if x in list:
	print ("exists")
else:
	print ("doesn't exist")