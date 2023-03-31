
def story():
    v=open('story.txt','w')
    count=0
    a='Things are happier when the world started its journey''\n'
    x=a.lower()
    b='then comes the man''\n'
    y=b.lower()
    c='tll the concepts get changed'
    z=c.lower()
    if x[0]!='t':
        count+=1
        pass
    if y[0]!='t' :
        count+=1
        pass
    if z[0]!= 't':
        count+=1
     


    v=open('story.txt','r')
    print(count)
    
    
    v.close()
story()