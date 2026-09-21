

**1.Extraction of digit**



n=5643

while n>0:

&#x20; lastDigit=n%10

&#x20; print(lastDigit)

&#x20; n=n//10



**2.Count digit**

n=5643

while n>0:

&#x20; lastDigit=n%10

&#x20; print(lastDigit)

&#x20; n=n//10

&#x20; 

&#x20; #Another way

&#x20; from math import \*

def countDigit(num):

&#x20; return int(log10(num))+1

n=countDigit(5687)

print(n)



**3..Reverse Number**

n=2347

num=n

reverse=0

while num>0:

&#x20; digit=num%10

&#x20; reverse=reverse\*10+digit

&#x20; num=num//10

print(reverse)



4**.Palindrome Number**

&#x20;  

n=22

num=n

reverse=0

while num>0:

&#x20; digit=num%10

&#x20; reverse=reverse\*10+digit

&#x20; num=num//10

if n==reverse:

&#x20; print("Palindrome")

else:

&#x20; print("Not palindrome")



**4.Armstrong Number**

&#x20;



**n=153**

**num1=n**

**total=0**

**length=len(str(n))**

**while num1>0:**

&#x20; **digit=num1%10**

&#x20; **total=total+(digit\*\*length)**

&#x20; **num1=num1//10**

**if total==n:**

&#x20; **print("Armstrong Number")**

**else:**

&#x20; **print("Not Armstrong")**

&#x20; 

&#x20; **#Another Way**

&#x20; 

**n=153**

**num=n**

**count=0**

**while num>0:**

&#x20; **digit1=num%10**

&#x20; **count+=1**

&#x20; **num=num//10**

**num1=n**

**total=0**

**while num1>0:**

&#x20; **digit=num1%10**

&#x20; **total=total+(digit\*\*length)**

&#x20; **num1=num1//10**

**if total==n:**

&#x20; **print("Armstrong Number")**

**else:**

&#x20; **print("Not Armstrong")**

&#x20; 





