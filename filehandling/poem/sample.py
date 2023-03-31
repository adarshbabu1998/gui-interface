def poem(a,b,c):
    s=open('poem.txt','w')
    s.write(a)
    s.write(b)
    s.write(c)
     
    s=open('poem.txt','r')
    print(s.read())
    s.close()
poem('tress are red''\n','rivers are blue''\n','that make all the differences''\n')
