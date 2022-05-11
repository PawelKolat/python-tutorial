from math import floor
from turtle import clear


clear

my_first_list = ["Pawel", "Janine", "Mila", "Boots"]
print("My list 1", my_first_list)

my_second_list=["Kora", "Lajka", 'Jip']
print("My list 2" , my_second_list)

my_first_list.extend(my_second_list)
print("My list 1 extended" , my_first_list)

my_second_list.insert(0, "Three legged dog")
print("My list 1 after insert" , my_first_list, "count of Three leegged dog: ",my_first_list.count("Three legged dog"))
print("My list 2 after insert", my_second_list, "count of Three leegged dog ",my_second_list.count("Three legged dog"))

my_second_list.append("Three legged dog")
my_second_list.append("Three legged dog")

print("My list 1 after insert" , my_first_list, "count of Three leegged dog: ",my_first_list.count("Three legged dog"))
print("My list 2 after append", my_second_list, "count of Three leegged dog ",my_second_list.count("Three legged dog"))

my_second_list.remove("Three legged dog")

print("My list 1 after remove" , my_first_list, "count of Three leegged dog: ",my_first_list.count("Three legged dog"))
print("My list 2 after remove", my_second_list, "count of Three leegged dog ",my_second_list.count("Three legged dog"))

while(my_second_list.__contains__("Three legged dog")):
    my_second_list.remove("Three legged dog")

print("My list 1 after while remove" , my_first_list, "count of Three leegged dog: ",my_first_list.count("Three legged dog"))
print("My list 2 after while remove", my_second_list, "count of Three leegged dog ",my_second_list.count("Three legged dog"))

mila_2=["Mila"] * 2

my_first_list.extend(mila_2)
print("Mila 3 times",my_first_list)

my_first_list_from_3=my_first_list[3:]
print("my_first_list_from_3", my_first_list_from_3)

while "Mila" in my_first_list_from_3:
    my_first_list_from_3.remove("Mila")
    

my_first_list=my_first_list[:3]
my_first_list.extend(my_first_list_from_3)
print("Mila 1 times", my_first_list)


numbers = [1,2,3,4,5]
numbers_to_3 = [number + 3 for number in numbers]
print(numbers_to_3)

#for each for in
my_first_list_each_appended=[person + "1" for person in my_first_list]
print("My list my_first_list_each_appended", my_first_list_each_appended)

list1=['a','b','c']
list2=list1

print("List object points to the same list", list1 is list2)

list1=['a','b','c']
list2=['a','b','c']
print("List object points to the same list", list1 is list2)

#floor
#mynumbers=[10,11,12,15,17]

# floor(mynumbers)

#exercises 

namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
namelist.append('pb122')
if 'pb122' in namelist:
    print("Now I know pb122!")


'''
print("Hello!")
# name = input("Enter youPr name: "), , makes it a tuple!!!
name = input("Enter youPr name: ")
print("Your name is " + name + ".")
'''

 
namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
#namelist = namelist.extend('theelous3')
namelist.extend('theelous3')
print(namelist)
if input("Enter your name: ") in namelist:
    print("I know you!")
else:
    print("I don't know you.")

