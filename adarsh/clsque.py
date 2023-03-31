#Define a class called "Person" with a constructor that takes in two parameters: "name" and "age". 
#The class should have a method called "introduce" that prints out "Hello, my name is [name] and I am [age] years old."

class person:
    def introduce(self,name,age):
        print('my name is ', name)
        print('i am',age,'years old')
object=person()
object.introduce('amal',99)
