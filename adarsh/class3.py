class sample:
    def display(self,name,age):
        self.age = age
        self.name = name # assign to self 
        print('my name is',name)
        print('my age is', age)
        print('my place is',self.place)

    def display2(self,place):
        self.place=place
        print('my name is',self.name)
        print('my place is', place)


obj = sample()

obj.display2('kochi')
obj.display('nisha', 19) 