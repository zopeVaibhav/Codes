#PRIME OR NOT
num = 23
# If given number is greater than 1
if num > 1:
# Iterate from 2 to n / 2
 for i in range(2, num//2):
#The number is not prime if 
#it is divisible by any no between 2 and n/2
  if (num % i) == 0:
   print(num, "is not a prime number")
   break
  else:
   print(num, "is a prime number")
else:
  print(num, "is not a prime number")
