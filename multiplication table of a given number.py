'''Write a program to print multiplication table of a given number'''

number= int(input("Enter number to get multiplication table: ")) #asking number and convert into integer
multi=1

while multi<=10:  #Run loop til value reach 10
    total=number*multi #Multipication 
    print("{0} * {1} = {2}".format(number,multi,total)) 
    multi+=1 #increment