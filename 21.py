from abc import ABC , abstractmethod 

class Animal (ABC):
    @abstractmethod
    def sound(self): # what is these 
        pass


class Dog(Animal):
    def sound(self):
        print("dog says:barks")


class Cat(Animal):
    def sound(self):
        print("cat says:Meow")



dog = Dog()
dog.sound()

cat = Cat()
cat.sound()