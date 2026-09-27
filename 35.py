class Dog:
    def __init__(self,name):  # define object born create 
        self.name = name 

    def bark(self):
        print("self.name say woow")

my_dog = Dog("buddy")
print(my_dog.name)
my_dog.bark()  



def Student(a, b):
    return a+b


answer= Student(10,20)

print(answer)