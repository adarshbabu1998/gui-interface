import re

p =input('ENTER YOUR PASSWORD:  ')
l=len(p)
count=0
s=r'[{A-Z}]'
x=re.search(s,string=p)
if x:
   count+=1
else:
    print('invalid','you missed upper characters')
    
d=r'[{0-9}]'
y=re.search(d,string=p)
if y:
      count+=1
else:
    print('invalid','you missed numbers')
    
n=r'[{@#$!%&*}]'
z=re.search(n,string=p)
if z:
     count+=1
else:
    print('invalid','you missed  special characters')
    
if l>=8:
    count+=1
else:
    print('invalid password ,less than 8 characters')
    pass
if count==4:
    print('valid')
