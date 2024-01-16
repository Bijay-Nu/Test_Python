class Temperature:
    def __init__(self,tem):
        self.tem = tem*1.8+35

    def Celsius(self):
        print(f'Fahrenheit is {self.tem}')

C = int(input('Enter Temperature of Degrees Celsius: '))
a = Temperature(C)
a.Celsius()


