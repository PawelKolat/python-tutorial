'''foundation = int(input("Enter number of bricks for your piramid foundation: "))
i=0
row =''
while i<foundation:
    i += 1
    row = row + str(i) + " "  
    print(row)


foundation = int(input("Enter number of bricks for your piramid foundation: "))
row_print=""
row_int = 0
foundation+=1
for column in range(1, foundation):
    column+=1
    for row in range(1, column):
       
        print(row, end=" ")
    print()
'''
#reverse


number_of_rows = int(input("Number: "))

for number in range(0, number_of_rows):
    #print(number)
    for column in range(number, number_of_rows):
        number+=1
        print(number, end=" ")
    print()
'''
for line_number in range(1, row_count+1):
       for number in range(line_number, row_count+1):
           print(number, end=' ')
       print()
'''