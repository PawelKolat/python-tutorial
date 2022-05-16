'''Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1

print("1", Money)
AddMoney()
print("2", Money)
'''
# solution 1
'''
Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print("1", Money)
AddMoney()
print("2", Money)
'''
# solution 2


Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   
   Money = 0 # assigned 
   Money = Money + 1
   print("locals xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx         ", locals())
   return Money # returned

print("1", Money)

print("2 returned", AddMoney())

print(dir(str))

print("globals yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy        ", globals())
size = 0
try:
   file = open("test1.txt", "w")
   file.write("This file is not that long")
   #OR
   #file = open("test1.txt", "r")
   ##text22 = file.read(0,file.tell())
   #text22 = file.read()
   #print(text22)
   #print(file.tell())

   
except:
   print("some error", str(size))
else:
   print("Ales clar", str(size))
finally:
   print("all done", str(size))


