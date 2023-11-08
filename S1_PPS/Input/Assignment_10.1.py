f=open("Vaibhav_0123.txt", 'r', encoding='utf-8')
#Finding The Position Of Cursor
print(f.tell())
#Bring File Cursor To Initial Point
f.seek(0)
print(f.tell())
#Reading Entire File
print(f.read())
f.seek(0)
#Reading File line-by-line
#Using for loop
for line in f:
    print(line,end="")
#Reading Individual Lines of Code
print(f.readline())
#Reading The Remaining Lines
print(f.readlines())
f.close
