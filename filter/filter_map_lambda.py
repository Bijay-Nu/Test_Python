# # syntax: filter(function, iterator[e.g:set,tuple,dict,list])

# a = [18,12,23,15,14,17,]
# def v(x):
#     if x>=18:
#         return False
#     else:
#         return True

# vv = list(filter(v,a))
# print(f'The students are Young enought to do work their age are {vv}')

############# Map ############

# syntax: map(function, iterable)

# a = [1,2,3,4,5]

# def maping_object(x):
#     return x+x
# val = list(map(maping_object,a))
# print(val)

############### lambda ############
# syntax: lambda(argument, expression)
# uppers = lambda string: string.upper()
# lowers = lambda string: string.lower()

# a = 'GeeksForGeek'

# print(uppers(a))
# print(lowers(a))

# format_numric = lambda num: f'{num}' if isinstance(num,int) else f"{num:,.2f}"
# print("Int formatting:", format_numric(90029))
# print("float formatting:", format_numric(999899.123))

# max = lambda a,b: a if (a>b)  else b
# print(max(1,2))

# def max(a,b):
#     if a<b:
#         return a # True
#     else:
#         return b
# print(max(1,2))

# a =12.122344
# b = '%.3f'%a
# print(b)

# b = 1.234
# print('%d'%d)

# a = 1
# while a<12:
#     print(' ')
#     a+=1
#     for i in range(1,11):
#         if a == 4:
#             continue

#         total = a*i
#         table_show = f'{a}*{i}={total}'
#         print(table_show)
#         pass
#     pass


#Write a Python function that takes two lists of integers as input and returns a new list containing only the numbers that are present in both lists, but with each number appearing only once in the final list.

# first_list = [1,2,3,4,5]
# second_list = [3,4,5,6,7,8]

# def marge_list(a,b):
#     new_list = list(set(a+b))
#     return new_list
# new_list = marge_list(first_list,second_list)
# print(f'This is the new list with the each number appearing only the once time in a final list\n {new_list}')

# a = 0
# while a< 5:
#     print(a)
#     a+=1
# else:
#     print('a is no longer less then 5')

# x = open('filter/my_demo.txt','r')
# print(x)



    



