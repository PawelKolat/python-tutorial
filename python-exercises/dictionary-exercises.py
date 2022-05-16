names_and_pets = [
    ('horusr', 'cats'),
    ('caisa64', 'cats and dogs'),
    ('__Myst__', 'cats'),
]
is_caisa = False
for item in names_and_pets:
    for inside_item in item:
        if('caisa' in inside_item):
            print("inside: ", inside_item)
            is_caisa=True
print(is_caisa)
if('horusr', 'cats') in names_and_pets:
    print("'horusr', 'cats' is there")
if(is_caisa):
    print("caisa is there")
else:
    print("it's not there")



names_and_pets_dictionary = dict(names_and_pets)
print(names_and_pets_dictionary)

print("keys: ", names_and_pets_dictionary.keys)
print("values: ", names_and_pets_dictionary.values)
print("values = cats")

new_dictionary = names_and_pets_dictionary.fromkeys('caisa64',"a")

print("new names_and_pets_dictionary ", names_and_pets_dictionary)
print("new dictionary ", new_dictionary)

if(names_and_pets_dictionary.get("caisa6")!=None):
    print("Value for caisa64: ",names_and_pets_dictionary.get("caisa64"))
else:
    print("No caisa64")

print(len(names_and_pets))

for one, two in names_and_pets:
    print("Name is {} and pets are {}".format(one, two))


## Limitations
"""
Sometimes it might be handy to use lists as dictionary keys, but it
just doesn't work. I'm not going to explain why Python doesn't allow
this because usually we don't need to worry about that.

```python
>>> stuff = {['a', 'b']: 'c', ['d', 'e']: 'f'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>>
```
"""
#lists cant be keys 
#stuff = {['a', 'b']: 'c', ['d', 'e']: 'f'}

#tuples work fine as dictionary
stuff = {('a', 'b'): 'c', ('d', 'e'): 'f'}

more_stuff = {"item1": "value2", "2":"two", "3": "three"}
print("stuff ", stuff)
print("more stuff ", more_stuff)

more_stuff_tuple_dictionary={("1", "one"): "jeden", ("2", "two"): "dwa"}

#todo
#question why is it returning one? - good exercise
all_keys =more_stuff_tuple_dictionary.get("1", "one")
print("all ", all_keys)

all_keys =more_stuff_tuple_dictionary.get(("1", "one"))
print("all ", all_keys)

#we want to go duck duck go duckgo go to be or not to be or go or should I stay
sentence = "we want to go duck duck go duckgo go to be or not to be or go or should I stay"

list_of_words = sentence.split()
words_dictionary_with_count = {}

for each in list_of_words:
    #todo addin and updating dictionaries for exercises
    words_dictionary_with_count[each] = list_of_words.count(each)
    print(each, "is ", list_of_words.count(each), "times")

sorted_words_dictionary_with_count= sorted(words_dictionary_with_count)
print("list {}".format(str(list_of_words)))
print("final dictionary: ", words_dictionary_with_count)
#print("sorted dictionary: ", sorted_words_dictionary_with_count)



