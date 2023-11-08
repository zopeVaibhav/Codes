n=int(input("Enter the number of inputs: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter the number: "))
    a.append(elem)
    
maxno=max(a)
minno=min(a)
sumno=sum(a)
avg=sum(a)/n

print("Maximum number is:" ,maxno)
print("Minimum Number is:" ,minno)
print("Sum of the all numbers is:" ,sumno)
print("Average of elements in the list",avg)

