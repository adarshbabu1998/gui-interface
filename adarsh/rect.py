# class rectu:
#     def prb(self,a,b):
        
#         area=a*b
#         perimeter= (2*a)+(2*b)
#         print('area of the rectange is',area)
#         print(' perimeter of the rectange is',perimeter)
# obj=rectu()
# obj.prb(a=int(input('enter the length of the rectange :')),
#         b=int(input('enter the breadth of the rectange :')))

#----------------------------------------------------

# simple inheritance parent class -> child class
# class office:
#     def display(self):
#         name='anisha'
#         print('my name is',name)

# class employee(office):
#     pass

# obj = employee()
# obj.display()



#----------------------------------------------------
# multple -- parent class -> 2 child cls
# class office:
#     def display(self):
#         name='anisha'
#         print('my name is',name)

# class employee(office):
#     def show(self):
#         print('hello')

# class manager(office):
#     def sample(self):
#         print('hai')
    

# obj = manager()
# obj2 = employee()
# obj.display()
# obj2.show()
# obj.sample()


# multilevel

class office:
    def display(self):
        name='anisha'
        print('my name is',name)

class employee(office):
    def show(self):
        print('hello')

class manager(employee):
    def sample(self):
        print('hai')


object = manager()
object.display()
object.show()
object.sample()

