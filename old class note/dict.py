name_of_stud = {
    "name":"Bijay Tamang",
    "age": "19",
    "Roll.No":"10",
    "DOB":"02/02/57"
}
# print(name_of_stud['name'])
# print(name_of_stud.get('age'))
# print(name_of_stud.values())
# print(name_of_stud.keys())
# print(name_of_stud.items())
name_of_stud['Addresh'] = 'Kathmandu'
name_of_stud.update({'Addresh':'kTM','age':'20'})

print(name_of_stud)

names = name_of_stud.copy()
names['Father Names'] = "Bj"
print(names)