import random

alp_small = 'abcdefghijklmnoqurstuvwxyz'
alp_upper = alp_small.upper()
numer = '0123456789'
symbol = "!@#$%^&*()'{,}:;<>'"

count = alp_small+alp_upper+numer+symbol
length = int(input('Enter the length of the password: '))
password = "".join(random.sample(count, length))
print(f'Your password is : {password}')
