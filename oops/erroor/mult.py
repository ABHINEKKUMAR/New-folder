with open("student.txt","r") as file:

    for line  in file:
        name,age =line.strip().split(",")


        print("Name:",name)

        print("Age:",age)