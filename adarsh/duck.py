# Create a Animal class with sound method that prints the sound of the animal. Then, create a Duck class that inherits from Animal and overrides 
# the sound method to print the quacking sound. 
# Then, create a MallardDuck class that inherits from Duck and overrides the sound method to print the mallard quacking sound.

class animal:
    def sound(self):
        name='cat'
        sound='meow'
        print('the animal is',name,'\n','the sound is',sound)
        


class duck(animal):
    def sound(self):
        name='duck'
        sound='quack'
        print('the animal is',name,'\n','the sound is',sound)
        


class MallardDuck(duck):
    def sound(self):
        name='mallard duck'
        sound='mquack'
        print('the animal is',name,'\n','the sound is',sound)
        

obj=MallardDuck()
obj.sound()




