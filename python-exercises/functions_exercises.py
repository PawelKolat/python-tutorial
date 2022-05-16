def do_this():
    print(something)

something = "this one"
do_this()


def do_this():
    something = input("put this in: ")
    print(something)


do_this()

def get_username():
    username = input("Username: ")
    print("username: ", username)

get_username()

def print_box(word, padding_char='*'):

    word_lenght=len(word)
    padding_side_length=int(word_lenght*30/2-word_lenght)
    print("padding", padding_side_length)
    print(padding_char*(((padding_side_length+word_lenght)*2)))
    print(padding_char* (padding_side_length+1),word,padding_char* (padding_side_length+1))
    print(padding_char*(((padding_side_length+word_lenght)*2)))
   
   
word="blah"
print_box(word)

print_box(padding_char="&", word="l")

name1=""
def ask_name():
        name1 = input("Enter your name: ")
        return name1

ask_name()
print("Your name is", ask_name())

def get_greeting():
    return "Hello World!"
print(get_greeting())

def greet(target):    
    print("Hello", target)

print(greet("World"))