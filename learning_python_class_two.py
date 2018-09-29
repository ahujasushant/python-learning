# Exercise 1
# Write a program to take an input integer and then take that many number of integers and print its multiplication by 2
# 4
# 3 8 10 5
# Output : 6 16 20 10

a = int(input())
for u in range(1,a+1): 
    b = int(input())
    print(b*2)
    
# Exercise 2
# Write a program to take 2 input numbers and print their sum
num_1 = int(input())
num_2 = int(input())
sum = num_1 + num_2
print(sum)


# Exercise 3
# Write a program to take N input numbers and print the sum of all. where N is input from user

num = int(input())
arr = []
for numbers in range(1,num+1):
    num_2 = int(input())
    arr.append(num_2)
print(sum(arr))


# Exercise 4
# Write a program to take N input numbers and print them in reverse. where N is input from user
# 5
# 1 6 8 2
# Output: 2 8 6 1
num = int(input())
arr = []
for numbers in range(num): # You can also do range(0, num) which is same as range(num)
    num_2 = int(input())
    arr.append(num_2)
arr.reverse()
print(arr)
print('Printing reverse of an array without using python revese method')
arr.reverse()
print(arr[::-1])


# Exercise 5
# Write a program to take N input numbers and print the sum of all. where N is input from user without using in-built sum function

num = int(input())

sum_of_numbers = 0
for numbers in range(1,num+1):
    num_2 = int(input())
    sum_of_numbers += num_2
print(sum_of_numbers)

# Write a function to print Hello world

def welcome_to_programming():
    print('Hello World')

welcome_to_programming()

# Write a function to take a input string and print it

def print_the_input_string(input_string):
    print(input_string)

print_the_input_string(input())

# Call the above function to print the input 10 times
def print_the_input_string(input_string):
    
    for i in range(0,10):
        print(input_string)

print_the_input_string(input())

# Now I want to print my input as many times as I want

def print_your_input(input_string, number_of_times):
    for i in range(number_of_times):
        print(input_string)

print_your_input(input(), int(input()))