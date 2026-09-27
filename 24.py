# class Student:
#      def __int__(self,name,roll,marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks

#      def display(self):
#         print("name",self.name)
#         print("roll",self.roll)
#         print("marks",self.marks)

#      s1 =Student("Rahul",1,85)  
#      s2 =Student("Ravi",3,90)    
#      s3 =Student("Priya",6,97)         


#      s1.display()
#      s2.display()
#      s3.display()


class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):  # function 
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)


s1 = Student("Rahul", 1, 85)
s2 = Student("Ravi", 3, 90)
s3 = Student("Priya", 6, 97)

s1.display()
s2.display()
s3.display()