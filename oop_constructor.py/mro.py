# class A:
#     def __init__(self):
#         super().__init__()
#         print('This is A')
    
# class B:
#     def __init__(self):
#         super().__init__()
#         print('This is B')

# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print('This is C')
# a =C()

# Write a Python function that takes a list of strings as input and returns a new list containing only the strings that are palindromes.

# def poli(a):
#     for i in range(0,int(len(a)/2)):
#         print(i)
#         if a[i]!= a[len(a)-i-1]:
#             return False
#     return True


# a ='malayalam'
# b  = poli(a)

# if b:
#     print('Yes')
# else:
#     print('None')

# x = lambda a,b,c : a+b+c
# print(x(6,2,3))

def myfun(n):
    return lambda a: a+n
a =myfun(2)
print(a(2))


