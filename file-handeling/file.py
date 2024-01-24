# file handeling
# file--> collection of data and information on disk permanently
# file type:
    # text file --> use to store in form character eg..txt,.py,.html,etc,eg=bijay1234
    # binary file --> sotre in the form of byte eg. image,video,pdf,audio
# file handeling --python perform a function such as create, read, write, append

# store data

# file handeling

# database

############# syntax:

# open(filename,mode,buffering,encoding,newline=None,error)
# code
# close
# mode-->purpose of opppening file
f = open("Bijay.txt",'r')
# a=f.read()
# a=f.readline()#read only one line
# a = f.readlines()
# print(a)
# f = open("Bijay.txt",'w+')
# f.write('Welcome to home!\n')
# f.write('Welcome to home!')
# a = f.readlines()
# print(a)

# f = open("Bijay.txt",'a')
# f.write('Welcome to home!\n')
# f.write('Welcome to home! \n')
# f.close
# print(f.name)
# print(f.mode)
# print(f.encoding)

#method
# print(f.readable)
# print(f.writable)
# try:
#     f = open('Bijay.txt','r+')
#     a = f.readlines()
#     print(a)
# except:
#     print('Please give a read mode')
# finally:
#     f.close()
#     print('The file is closed')

with open('Bijay.txt','w') as f: # in the with statement the file will close auto mathicaly
    f.write('This is the new line of the code')
    # f.close()
print(f.closed)


