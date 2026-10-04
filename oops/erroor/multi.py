n= int(input("how many student"))

with open ("student.txt","w") as file:
    for i in range(n):
        print("student ",i+1)
    name =input("eneter name")
    age =input("eneter age ")

    file.write(name +","+age)

print("all student data saved ")