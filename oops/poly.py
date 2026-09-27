

# same name with different argument 
class Dog:
     def sound(self):
        print("dog is barking")

class Cat:
    def sound(self):
        print("cat is meow meow")

class Cow:
     def sound(self):
        print("cow is maa")

animal = [Dog(),Cat(),Cow()]

for animal in animal:
     animal.sound()

