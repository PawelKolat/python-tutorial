from tracemalloc import start


auto_tuple=1, 2

print(auto_tuple)

[a, b] = (1, 2)

print(a, end=" ")
print(b)

items = [('a', 1), ('b', 2), ('c', 3)]
for pair in items:
    x, y = pair
    print("line 1: ",x, y)


for r,t in items:
    print("line: ",r, t)


presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]

i=1
for president in presidents:
    
    print(str(i)+ " President of the US was {} was even though {} was a poor dude".format(president, president))
    i+=1

for num, name in enumerate(presidents, start=1):
    print("The {} was the named {} after an old clock".format(num, name) )

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))
print("with zip")
for colour,ratio in zip(colors, ratios): 
    print("{}% {}".format(ratio * 100, color))

#exercises
something_str="something"
something_list=[]
while something_str != "":
    something_str=input("Enter something, and press Enter without typing anything when you're done.")
    something_list.append(something_str)
something_list.remove("")
for counter, item in enumerate(something_list, start=1):    
    print("Line", item, "is: ", counter)


uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

print("zip no enum")
counter_1=0
for upper_letter, lower_letter in zip(uppercase, lowercase):
        counter_1+=1
        print(counter_1, upper_letter, lower_letter)


print("zip and enum")
for counter_1, upper_letter_lower_letter in enumerate(zip(uppercase, lowercase), start=1):
        print(counter_1, upper_letter_lower_letter)



print("zip and enum 2")
uppper_lower_zip=zip(uppercase, lowercase)
for index, pair in enumerate(uppper_lower_zip, start=1):
    each1, each2=pair
    print("here", index, each1, each2)


print("zip and enum 3")

enum_upper=enumerate(uppercase, start=1)
zip_enum_upper_lower = zip(enum_upper, lowercase)

for enum_upper, lower_enum in zip_enum_upper_lower:
    index, upper = enum_upper
    print(index, upper, lower_enum)

print("playground")
for a, b in zip(uppercase, lowercase):
    print(a,b)


### from answers
'''
print("zip 4")
for upper, indexlowerpair in zip(uppercase, enumerate(lowercase, start=1)):
    index, lower = indexlowerpair
    print(index, upper, lower)
    '''