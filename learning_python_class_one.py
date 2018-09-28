# Enter your code here. Read input from STDIN. Print output to STDOUT

# Exercise 1
# Write a program to print 'Hello World' in Python

print("Hello World")

# Exercise 2
# Write a program to print numbers from 0 to 9 in Python

# Using while loop
print('Printing using while loop')
n = 0
while n < 10:
    print(n)
    n += 1

# Using for loop
print('Printing using for loop')
for i in range(0,10):
    print(i)
    
# Exercise 3
# Write a program to print numbers from 0 to 9 in same line separated by comma in Python 0,1,2,3,4,5,6,7,8,9
print('Printing on same line')
for i in range(0,10):
    print(i, end=',')

# Exercise 4
# Write a program to print multiplication table of 7 in same line separated by comma in Python 7, 14, 21, ... 70
print('Multiplication table of 7 using while loop')
a = 7
n = 1
while n < 11:
    print(a*n, end=',')
    n += 1
    
print('Table of 7 using for loop')
a = 7
for i in range(1,11):
    print(a*i, end=',')
    
# Exercise 5
# Write a program to store, store table of 6 in a list/array 
L = [1,2,3]
print(L) # 1,2,3

a = 6
table = []
for i in range(1,11):
    table.append(a*i)

print(table) # 6, 12, 18..60

# # Exercise 5
# # Write a program to store table of 9 in a list/array in reverse order
a = 9
table = []
for i in range(1,11):
    table.append(a*i)

table.reverse()
print(table) # 90, 81, .... 18, 9

# Exercise 6
# Just print numbers from 1 to 10 in reverse order 10, 9, 8, 7, ... 1

for i in range(10, 0, -1):
    print(i, end=',')
    
print('Multiplication table of 9 in reverse order')

initial_number = 9
for i in range(10, 0, -1):
    print(initial_number, 'X', i, '=', initial_number * i)

print('Multiplication table of 9 in reverse order without using * ')

initial_number = 9
for i in range(90, 8, -9):
    print(initial_number, 'X', i//9 , '=', i)
