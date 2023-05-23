import platform

name = input("please enter your name")
birthday = input ("please ennter your birthday")

f1 = open("data.txt", "a+")
f1.write(name)
f1.write(birthday)
