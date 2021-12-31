'''Print list in reverse order using a loop'''
list1 = [10, 20, 30, 40, 50]
print(list1[::-1]) #print list in reversed order by slicing method
newlist= reversed(list1) #Reversed inbuilt function reverse the list and store in new variable
for list_item in newlist: #store list item into list_item variable
    print(list_item) #print every list item using for loop
    

