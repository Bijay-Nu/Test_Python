# slicing is the part of accessing the data
# a ='Bijay'
# print(a[::-1])
# a = 'Bijay'
# b = 24.234
# print(f'I have a number {b:.3f}')
# print('My name is {} and I am {} Years Old'.format(a,b))


class Coffee:
    def coffee(new_coffee,Refill,Drink):
        if (new_coffee=="Empty"):
            Coffee.Refill()
        else:
            Coffee.Drink()
coffee = Coffee()
