# Q5
exit_list=[1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
unique_list=[]
# using loop 
for i in exit_list:
    if not(i in unique_list):
        unique_list.append(i)
# print the list of unique
print("Enter the Unique list:",unique_list)        
