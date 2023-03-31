def file2():  
        s=open('create.txt','r')
        print(s.read())
        s.close()
        
#------------------------------
def file1(a):
        s=open('create.txt','w')
        s.write(a)
#------------------------------
def end(b):
       s=open('create.txt','a')
       s.write(b)
#------------------------------ 
i=0
while True:
        print('choices are: ','\n','1.write','\n','2.read','\n','3.append','\n','4.overwrite','\n','5.exit')
        choice=int(input('enter your choice: '))
        
        if choice==1:
                file1(input('enter your text:'))
        elif choice==2:
                file2()
                break 
        if choice==3:
                end(input('enter your text you want to append:'))
        elif choice==4:
               file1(input('enter your text:'))
               
        if choice==5:
               break
