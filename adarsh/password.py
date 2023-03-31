p=input('enter your password: ')
l=len(p)
char=['!','@','#','%','*','&']
num=['1','2','3','4','5','6','7','8','9','0']
if l<8:
        print('invalid password')
pass
for i in p:
        if i in num:
                print('valid password')
                pass
        if i in char:
                print('valid password')
       