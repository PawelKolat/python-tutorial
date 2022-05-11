variable1=input("something 1: ") 
variable2=input("something 2: ")
if(variable1.__contains__(variable2)):
    print("variable 1 contains variable 2" + variable1, " contains ", variable2)
if(variable2.__contains__(variable1)):
    print("variable 2 contains variable 1")