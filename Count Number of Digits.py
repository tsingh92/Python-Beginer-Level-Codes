'''Write a program to count the total number of digits in a number using a while loop.'''
digit=int(input("Enter the digit you want to count number: "))
i=0
digit=str(digit)
while i<len(digit):
    i+=1
print("The total number of digits are : {}".format(i))