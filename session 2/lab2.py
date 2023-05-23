
print ('''
choose the number of the function you want to understand
	
1- center()	
2- count()	
''')

num = int(input("enter your number"))

string = input("enter a string")

if num == 1:

	print ('''this function get your string at the center with the number you choose 

lets choose 10 for your string	

	as for the string you entered the output will be :
	''')

	print( string.center(10))

if num == 2:

	print ('''this function print the number a letter of your string is repeated

	as for the string you entered i will count the 'a'
	and the output will be  :
	''')

	print (string.count('a'))