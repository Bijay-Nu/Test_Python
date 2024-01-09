a = 'Welcome to Game, Made by Bijay, Using pytohn'
print('\n \n \n \n',a.center(70,'-'))
b = '''
S for Sissor,
P for paper,
R for Rock
'''
print(b)
print('Remenber ! S>P, P>R, R>S')
user=input('Enter Your choice:\n==>')
user=user.upper()
print(f'Your Choise {user}')

import random
computer = random.choice(['S','R','P'])
print(f'Computer Choose {computer}')

if (user=='S' and computer=='P') or (user=='P' and computer=='R')or\
(user=='R' and computer=='S'):
    print('Your won !!')
elif user == computer:
    print('Draw!')
elif user not in ['S','R','P']:
    print('Your intre key is wrong')
else:
    print('Compputer won!!')
