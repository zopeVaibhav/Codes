#Opening A File Using Python
f=open("Vaibhav.txt")              
f=open("C:\Users\vaibh\OneDrive\Desktop\PPS Assignments\Input\Vaibhav.txt") 
#Closing File
f=open("Vaibhav.txt")
f.close
#Writing in File
f=open("Vaibhav.txt", 'w', encoding='utf-8')
f.write("This Is My First File.\n")
f.write("This File was Created Just Using Python!!. \n")
f.write("This File Has 3 Lines. \n")
f.close
#Reading File 
f=open("Vaibhav.txt", 'r', encoding='utf-8')
print(f.read(0))
print(f.read(0))
print(f.read())
f.close
