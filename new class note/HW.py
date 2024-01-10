# 1.Create a list by picking an odd-index items from the first list and even index items from the second in one third list 
# first_list = [1,45,3,5,6,7,56,7,45,45,6]
# second_list = [34,5,36,3,6,7,18,346,87,8]

# odd_number = []
# even_number =[]

# for i in first_list:
#     if (i%2!=0):
#         odd_number.append(i)
    
# print('odd_number:',odd_number)

# for i in second_list:
#     if (i%2==0):
#         even_number.append(i)
# print('Even number:',even_number)

#########################################################

# Qn no.2
# 2.Get all values from the dictionary and add them to a list but don’t add duplicates

# names = {
#     'name':'Bijay',
#     'age':18,
#     'address':'ktm,lalitpur'
# }
# lists=[18,24,6,7,12,34,4,6,720,19,23]
# for i in names.values():
#     lists.append(i)
# rm_dup = list(set(lists))
# print(rm_dup)

# 3.Remove duplicates from a list and create a tuple and find the minimum and maximum number
# num = [12,23,4,2,4,5,12,35,4,54,4,3,5,6,7,4]
# new_list =set(num)
# a = sorted(new_list)
# tup = tuple(a)
# print(f'Minimum number is {tup[0]}')
# print(f'Maximum number is {tup[-1]}')

# 4.WAP to check wheather the last digit of a number(enter by user ) is divisible by 3 or not

# number = input("Enter the numbers\n==>")
# num = int(number[-1])
# print(num)
# if num%3==0:
#     print('The last number is divisible!! by 3')
# else:
#     print('the last number is not divisible** by 3')


# l1 = [2,10,11,25,234,34,20]
# l2 = [1,2,3,4,5,6,6,12,54]

# def new_list(l1,l2):
#     t_list = list(set(l1+l2))
#     return t_list

# new_l = new_list(l1,l2)
# print(f'\n\nNew list is: {new_l}\n\n')

   
    



    






        

