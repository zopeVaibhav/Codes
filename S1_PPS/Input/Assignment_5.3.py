#factorial computation
n = int(input("Enter any number:"))
fact = 1
for i in range(1,n+1):
 fact = fact*i
print ("The factorial of",n," is : ",end="")
print (fact)

#METHOD 2
# Python code to demonstrate math.factorial()
import math
n=int(input("Enter any number:"))
m=math.factorial(n)
print("The factorial of",n,"is:",m)
