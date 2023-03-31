#  global , local

name = 'adarsh' # global variable


def sample():
    print('my name is', name)

def sample2():
    print(name)

def sample3():
    age = 17 # local variable
    print('my age is', age)
    def sub_func():
        print(age)
    sub_func()

def sample4():
    print(age)

sample()
sample2()
sample3()
sample4()