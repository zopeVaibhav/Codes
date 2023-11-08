English  =int(input("Enter marks of the English : "))
Math     =int(input("Enter marks of the Math : "))
Physics  =int(input("Enter marks of the Physics : "))
Chemistry=int(input("Enter marks of the Chemistry : "))
Biology  =int(input("Enter marks of the Biology : "))
avg      =(English+Math+Physics+Chemistry+Biology  )/5
print("Average of all the above entries is : ",avg)

if(avg>=75):
 print("Grade: A")
elif(avg>=60 and avg<75):
 print("Grade: B")
elif(avg>=50 and avg<60):
 print("Grade: C")
elif(avg>=40 and avg<50):
 print("Grade: D")
else:
 print("Grade: Fail")