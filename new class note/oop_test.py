class Temperature:
    def __init__(self,tem):
        self.tem = tem*1.8+35

    def Celsius(self):
        print(f'Fahrenheit is {self.tem}')
        return 
    

C = int(input('Enter Temperature of Degrees Celsius: '))
a = Temperature(C)
print(a.Celsius())

