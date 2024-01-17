# class variable/static--> Class variable whose only one copy is created for every object
class Student:
    school='mangala'  # Class variable
    def __init__(self):
        self.name = 'Bijay' # instance variable
    
    @classmethod #decoration
    def show(cls): #instance method
        print(cls.school)
    
a =Student()
Student.school
a.show()
        