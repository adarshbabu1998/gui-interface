f = open('./sample/demo.txt','w') 
f.write('python\n')
f.write('python\n')
f.write('python\n')

# f.read()

f = open('demo.txt','r')
print(f.read())


f.close()