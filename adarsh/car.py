# Create a Vehicle class with start and stop methods. Then, create a Car class that inherits from Vehicle and has an additional attribute num_wheels. 
# Implement the start and stop methods for Car class to print appropriate messages.

class vehicles:
    def start(self):
        method='starts'
        print('the car is',method,'now')
    def stop(self):
        methods='stop'
        print('the car is',methods,'now')
class car (vehicles):
    def num_wheels(self):
        wheels=5
        print('the car has',wheels,' wheels now')

obj=car()
obj.start()
obj.stop()
obj.num_wheels()
    
