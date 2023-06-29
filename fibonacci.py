#Python progam to check fibonacci number

# First two fibonacci terms
fib_nums = [0, 1]  

number = int(input('Enter the number you want to check for fibonacci number: '))

# Iterate fibonacci terms until the user number is reached
while fib_nums[-1] <= number:
    fib_nums.append(fib_nums[-1] + fib_nums[-2])
#Printing the result whether the given number is fibonacci or not
if number in fib_nums:
    print(f'Yes. {number} is a fibonacci number.')
else:
    print(f'No. {number} is NOT a fibonacci number.')
