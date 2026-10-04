# taking dat from the user and store 


name =input("eneter a name ")
age =(input("enter a age "))

with open("student.txt","w")as file:
    file.write("name"+name+"\n")
    file.write("age" +age+"\n")

print("student information")