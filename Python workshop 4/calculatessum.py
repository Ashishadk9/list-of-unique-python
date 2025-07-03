#Q2
# Input
N =int(input("Enter the element number:" ))
# Store a number
numbers =[]
# input the N numbers
for i in range(N):
    num=int(input("Enter a number:"))
    numbers.append(num)
# Calculate the sum
sum_of_odd=0
sum_of_even=0
# Calculate the sum of odd and even numbers
for num in numbers:
    if num % 2 == 0:
        sum_of_even += num
    else:
        sum_of_odd += num
# print the output
print("Sum of odd numbers:", sum_of_odd)
print("Sum of even numbers:", sum_of_even)