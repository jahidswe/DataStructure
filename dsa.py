#palindrome number
n=131
num=n
reverse=0
while num>0:
  digit=num%10
  reverse=reverse*10+digit
  num=num//10
if n==reverse:
  print("Palindrome")
else:
  print("Not palindrome")

#Armstrong Number

n=153
num1=n
total=0
length=len(str(n))
while num1>0:
  digit=num1%10
  total=total+(digit**length)
  num1=num1//10
if total==n:
  print("Armstrong Number")
else:
  print("Not Armstrong")
  
  #Another Way
  
n=153
num=n
count=0
while num>0:
  digit1=num%10
  count+=1
  num=num//10
num1=n
total=0
while num1>0:
  digit=num1%10
  total=total+(digit**length)
  num1=num1//10
if total==n:
  print("Armstrong Number")
else:
  print("Not Armstrong")
  

