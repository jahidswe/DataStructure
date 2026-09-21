#count Digit
n=5643
while n>0:
  lastDigit=n%10
  print(lastDigit)
  n=n//10
  
#Another way
from math import *
def countDigit(num):
  return int(log10(num))+1
n=countDigit(5687)
print(n)