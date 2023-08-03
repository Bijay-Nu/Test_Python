mylist = []

a = int(input("How many number you have:\n"))
for i in range(a):
    b = int(input("Enter the nubmer: "))
    mylist.append(b)

sq = [j *j for j in mylist]
print(sq)
    

