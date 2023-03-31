import re
s=input('eneter a string: ')
l=len(s)
count=0
y=r'[{a,e,i,o,u}]'

for i in s:
    m=re.search(y,string=i)
    if m:
        count+=1
print(count)