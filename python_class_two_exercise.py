# Write a program that asks the user for their name and greets them with their name.

def print_users_name(name):
    print('Hello' + ' ' + name)

print_users_name(input())

# Modify the previous program such that only the users Alice and Bob are greeted with their names.

def print_users_name(name):
    if name == 'Alice' or name == 'Bob':
        print('Hello' + ' ' + name)

print_users_name(input())

# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

def print_sum(number):
    sum_of_numbers = 0
    for i in range(1,number+1):
        sum_of_numbers += i
    print(sum_of_numbers)

a = int(input())
print_sum(a)

# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

def print_sum(number):
    sum_of_numbers = 0
    for i in range(1,number+1):
        if i % 3 == 0 or i % 5 ==0:
            sum_of_numbers += i
    print(sum_of_numbers)

print_sum(17)

# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.




def product_or_sum(number, answer):
    sum_of_numbers = 0
    product_of_numbers = 1
    for i in range(1,number+1):
        sum_of_numbers += i
        product_of_numbers = product_of_numbers * i
        
    if answer == "true":
        print(sum_of_numbers)
    elif answer == "false":
        print(product_of_numbers)
    else:
        print('Answer must be true or false')
    
a = int(input())
b = input()
product_or_sum(a,b)


# Write a program that prints a multiplication table for numbers up to 12.

for i in range(1,13):
    for a in range(1,11):
        b = a * i
        print(b)
        
# Write a function that returns the largest element in a list

list = [12,23,434,54,6567,6,87,8,7,8,9,8,9,98,6,45,64,3]
print(max(list))

# Write a function that checks whether an element occurs in a list
list = [12,23,434,54,6567,6,87,8,7,8,9,8,9,98,6,45,64,3]
def check_list(element):
    if element in list:
        print(element, 'exists in the list')
    else:
        print(element, 'is not present in the list')
        
check_list(54)

# Write a function that returns the elements on odd positions in a list.
list = [12,23,434,54,6567,6,87,8,7,8,9,8,9,98,6,45,64,3]
def grab_odd_positions():
    a = list[1::2]
    print(a)
    
grab_odd_positions()