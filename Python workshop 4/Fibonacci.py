# Q4
# Print number
N = int(input("Enter how many Fibonacci numbers to print: "))
# Two fibonacci numbers
a, b = 1, 1
fib_num = []

for i in range(N):
    fib_num.append(a)
    print(a, end=' ')
    a, b = b, a + b

# Optional: print the list
# print("\nFibonacci sequence:", fib_num)