'''Display numbers from a list using loop
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop'''
numbers = [12, 75, 150, 180, 145, 525, 50,100,95]
for i in numbers:
    if i%5==0 and i<=500:
        if i<=150:
            print(i)