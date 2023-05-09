#list
y =input("enter sensor readings").split("&",4)
list = [1,6,7]
#add to list
list.extend(y)
list.remove("1")
list.insert(0,20)
print(list)
#tuble
tuble = (y)
print (y)
#dictionary
dictionary={
			" readinsensor 1" : y[0],
			"readinsensor 2" : y[1],
			" readinsensor 3" : y[2],
			" readinsensor 4" : y[3]
			}
print (dictionary)

