
def ucln(a,b):
    while a!=b:
        if a>b:
            a=b-a
            print(a)
        else:
            b=b-a
            print(b)

    return b

print(ucln(16,72))