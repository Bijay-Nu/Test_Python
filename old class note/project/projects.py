# Write a program in Python to print your own name using function.
'''
def name():
    my_name={
        'name':'Bijay Tamang',
        'age':18,
        'address':'Bhanimandal'
    }
    for i in my_name.items():
        print(i)

name()

'''
# Write a program in Python to print even numbers between intervals using function
'''
def even_num():
    list_of_even_num = []
    for i in range(1,10):
        even_number=i%2
        if even_number==0: 
            list_of_even_num.append(i)
    print(f'Even Numbers are:\n{list_of_even_num}')
    return
even_num()
'''

# Write a program in Python that generates random password.
'''import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
number = '01234566789'
symbol = '}_=-+/<!@>#$%^*(){[]\\&'

combination = upper + lower + number + symbol
length = int(input('Enter the length of Password you wnat to generate\n=>'))

password = "".join(random.sample(combination,length))
print(f'Your password is: {password}')'''
        
# Write a program in Python that find the area of a circle using function.
'''
pi_value = 3.14
r =5
def circle_area(pi_value,r):    
    area = pi_value*r**2
    print(f'Area of circle is {area}')
    return
circle_area(pi_value,r)
'''

# Write a program in a Python that implements the Pythagorean theorem using function.
'''
a = 5
b = 6
def pythogerous(a,b):
    h = a**2 + b**2
    h = h**0.5
    print(h)
    return
pythogerous(a,b)
'''
# Write a program in Python to reverse a String using function.

'''
# step1
a = '123'
def reverse(a):
    for i in a[::-1]:
        print(i,end='')
    return
reverse(a)
'''
# step2

'''def reverse(x):
    return x[::-1]
out_come=reverse('1234567')
print(out_come)'''

# Write a program in Python to calculate power of a certain number. For e.g 5^3=125

'''
a= 24
p = a**2
print(f'Power of {a} is {p}')

b=4567
p_b =b**4
print(f'Power of {b} is {p_b}')
'''
# Write a program to print your name in Python.
'''
a = 'Bijay Tamang'
print(a)
'''

# Write a program to print Hello I am “John Doe” and Hello I’am “John Doe” with single and double quotes.

'''
print('Hello I am “John Doe”')
print('Hello I\'am “John Doe”')
print("'Hello I\'am 'John Doe'")
'''
# Declare constant type** of int set value 7.

'''
a = 7**2
print(a)
'''

# Write a program in Python that finds simple interest. Formula= (p * t * r) / 100
# Formula= (p * t * r) / 100

'''
p = int(input('Enter the value of P=Princiaal\n=> '))
r = int(input('Enter the value of R=Rate of interest\n=> '))
t = int(input('Enter the value of T=Time\n=> '))
cal_si = p*r*t
si = cal_si/100
print(f'Simple intrest is {si}')

 '''
# Write a program to print a square of a number using user input.
'''
a = int(input('Ente the number to find it\'s square\n=> '))
sq_of_num = a*0.5
print(f'Your square value {a} is {sq_of_num}')
'''
# Write a program to print full name of a from first name and last name using user input.
'''
fname = input('Enter you first name: ')
lname = input('Enter you last name: ')

fullname = fname + ' ' +  lname
print(f'Your full Name is {fullname}')
# methos 2 another
print(f'Your full Name is {fname} {lname}')

'''
# Write a program to find quotient and remainder of two integers.
'''
n1 = int(input('Enter the first value: '))
n2 = int(input('Enter the second value: '))
Q = n1//n2
rem = n1%n2
print(f'Quotients vanue is {Q} an the reminder is {rem}')
'''
# Write a program to swap two numbers
'''
a = 2
b = 3

c = a
b =c

print(b)
'''
# Write a program in Python to remove all whitespaces from String.

'''a = ' Hello world '
b = a.strip()
print(b)
'''
# Write a Python program to convert String to int.
'''strings = '2'
print(type(strings))
integers = int(strings)
print(type(integers))'''

 
# Suppose, you often go to restaurant with friends and you have to split amount of bill.
# Write a program to calculate split amount of bill. Formula= (total bill amount) / number of people

'''num_of_per = int(input("Enter the numer of People: "))
amount__bill = int(input("Enter the Amount of Bill: "))
total_amount = amount_of_bill / num_of_per
print(f"Rs.{total_amount} should pay per person")'''
# Write a Python program to check if the number is odd or even.

'''number = int(input('Enter the number: '))
total  =  number % 2
if total ==0:
    print(f'{number} is the Even number')
else:
    print(f'{number} In the Odd number')'''


# Write a Python program to check whether a character is a vowel or consonant.
'''character  = input('Enter the Character: ')
vowel = ('a','e','i','o','u')
if character in vowel:
    print('Vowel')

else:
    print('Consonant')'''


for i in range(100):
    if i ==41:
        continue
    print(i)
    




