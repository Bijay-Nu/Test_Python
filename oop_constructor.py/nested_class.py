# class Student:
#     def __init__(self):
#         self.name = 'Bijay'
#         self.d =self.Std()

#     def show(self):
#         print(self.name)
#     # new class
#     class Std:
#         def __init(self):
#             self.age=18

#         def show1(self):
#             print(self.age)

class A:
    def student(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    
    def printname(self):
        print(f'Yoru Full Name is: {self.first_name} {self.last_name}')

class B(A):
    def info(self,fname,lname):
        A.__init__(fname,lname)

a = B()
a.student('Bijay','Tamang')
a.printname()

    