#Print Natural Numbers from 1 to User Choice While Loop
print("Welcome to Printing Natural Number from 1 to Your choice number.")
number= int(input("Enter the number: "))
number_in_list=[]
num=1
while num<=number:
    number_in_list.append(num)
    print(num)
    num+=1
    
print("Natural Number in list as follows:")
print(number_in_list)

