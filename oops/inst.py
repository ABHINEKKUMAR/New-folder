# parent class
class Animal:

     def eat(self):
        print("Animal is eating")

     def sleep(self):
        print("Animal is sleeping")

# child class 
class Dog (Animal): # paremeter of parent 
     def bark(self): # self current instance 
        print("dog is barking")

dog= Dog()


dog.eat()
dog.sleep()
dog.bark()