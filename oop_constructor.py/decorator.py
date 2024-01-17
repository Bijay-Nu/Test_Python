def show():
    def inner(v):
        print('Hello world')
        return v
    return inner
@show()
def display():
    print('welcome to y channel')
display()
