class Student:
    def __init__(self):
        self.name = 'Bijay'
        self.age = 18

    def show(self):
        print('Your name is:',self.name)

    def show1(self,email):
        self.email = email
        print('Age:',self.age,'\nEmail:',self.email)

a=Student()
a.show()
a.show1("Helloworld@gmail.com")

