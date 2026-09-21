#reverse number
n=2347
num=n
reverse=0
while num>0:
  digit=num%10
  reverse=reverse*10+digit
  num=num//10
print(reverse)
