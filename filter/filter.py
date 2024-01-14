age = [5,12,17,18,24,32]

def my_function(x):
    if x<18:
        return False
    else:
        return True
    
tenage = filter(my_function,age)
for x in tenage:
    print(x)


