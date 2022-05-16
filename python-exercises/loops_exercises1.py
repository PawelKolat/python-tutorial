something = "Started"
while something != "":
    something = input("Enter something: ")
    print(something)

something_bool = False
while not something_bool:
    something = input("Enter rain or sun: ")
    if('rain' in something):
        something_bool = False
        print("you entered: ", something, "and it's raining, I'll keep at it till it's sunny or something else") 
    elif('sun' in something):
        something_bool = True
        print("you entered: ", something, "and it's sunny") 
    else:
        something_bool = True
        print("you entered: ", something, "and it's", something) 

stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

#######

for item in stuff:
    print("for ", item)

i=0
while i < len(stuff):
    print("While ", stuff[i])
    i += 1


'''
There's only one big limitation with for looping over lists. We
shouldn't modify the list in the for loop. If we do, the results can
be surprising:
'''


for thing in stuff:
    stuff.remove(thing)
print(stuff)

something = "Started"
while something != "":
    something = input("Enter something: ")
    print(something)

something_bool = False
while not something_bool:
    something = input("Enter rain or sun: ")
    if('rain' in something):
        something_bool = False
        print("you entered: ", something, "and it's raining, I'll keep at it till it's sunny or something else") 
    elif('sun' in something):
        something_bool = True
        print("you entered: ", something, "and it's sunny") 
    else:
        something_bool = True
        print("you entered: ", something, "and it's", something) 

stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

#######

for item in stuff:
    print("for ", item)

i=0
while i < len(stuff):
    print("While ", stuff[i])
    i += 1


'''
There's only one big limitation with for looping over lists. We
shouldn't modify the list in the for loop. If we do, the results can
be surprising:
'''


for thing in stuff:
    stuff.remove(thing)
print("old", stuff)

stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

for thing in stuff.copy():
    stuff.remove(thing)
print("new", stuff)

### exercises

''' fix
things = str([1, 2, 3, 4, 5])
for thing in things:
    print(thing)
'''
'''
things = [1, 2, 3, 4, 5]
for thing in things:
        print(thing)


before = [[1, 2], [3, 4], [5, 6]]
after = []
for number in before:
    after.extend(number)
print(after)
'''
input = ['1', '2', '3']
numbers = []
for string in input:
    numbers.append(int(string))
print("numbers",numbers)
print("str", string)    
result = 0
for n in numbers:
    result += n
print("their sum is", result)

numbers = ['1', '2', '3']
for number in numbers:
    numbers[numbers.index(number)] = int(number)
print(numbers)

numbers = ['1', '2', '3']
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))



