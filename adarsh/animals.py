# Create a Animal class with sound method that prints the sound of the animal. 
# Then, create Dog and Cat classes that inherit from Animal and override the sound method to print the barking and meowing sound respectively.

class animal:
    def sound(self,name,sound):
        if name=='dog':
            print('the animal is',name,'\n','the sound is',sound)
            pass
        

class dog(animal):
    def second(self,name2,sound2):
         if name2=='cat':
            print('the second animal is',name2,'\n','the sound is',sound2)
    pass
class cat(animal):
    pass

obj=dog()
obj.sound(input('enter the name of animal: '),'bow bow')
obj.second(input('enter the name of animal: '),'meow meeeowwww')

