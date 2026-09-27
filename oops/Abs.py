from abc import ABC , abstractmethod 

class Animal(ABC):

    @abstractmethod #create abstract method
    def sound(self):
        return # value pass 
        # these is def function(self) current instance # pass  # pass value 

class Dog(Animal):
    def sound(self):
        print("dog say wowow")

class Cat(Animal):
    def sound(self):
        print("cat say meow")

dog =Dog() 
cat =Cat()

dog.sound()
cat.sound()