class Person:
    name ="Rahul"  # data member

    def show_name(self):
        print("name",self.name)

class Student(Person):
    def study(self):
        print("student is studying")

s =Student()
s.show_name()
s.study()
