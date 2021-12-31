'''Write a program to display all prime numbers within a range'''

start=int(input("Enter start number: "))
while True:  #while condition is true ask end number
    end= int(input("Enter end number: "))
    if start<end: #if end number greater than start number
        for num in range(start,end):
            if num>1: #whole number start from 1 or greater than 1
                for num2 in range(2,num):
                    if num%num2==0: #if number divide then loop break
                        break
                else: #if number not divide then print the number
                    print(num)
        break
    else: #if statement wrong start>end
        print("Enter end number greater than start number!")

        
                