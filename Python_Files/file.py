#f=open("C:\Users\Windows10\Downloads.Steve.jpg",mode = 'r',encoding = 'cp1252')
#f.close()

#try:
    #f = open("main.py",encoding = 'utf-8')
    #finally:
        #f.close()

with open("C:\Users\Windows10\Documents\Python_Files\test.txt",'w',encoding = 'cp1252') as f:
    f.write("my first file\n")
    f.write("This file\n")
    f.write("contains three lines\n")

f = open("test.txt",'r',encoding = 'utf-8')

#read the first 4 data
print(f.read(4))

#read the next 4 data
print(f.read(4))

print(f.read())


#the current file position
print(f.tell())


#bring the file cursor to the initial position

f.seek(0)


for line in f:
    print(line, end = '')
    
print(f.readline())