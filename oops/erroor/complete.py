# # #all the thing in one plaace 
# # while True:
# #     print("Student file ")
# #     print("1. Add student")
# #     print("2. view student")
# #     print("3.exit")

# #     choice =input("enter a choice ")

# #     if choice =="1":
# #         name = input("enetr a name")
# #         age =input("enter a age ")

# #     with open("student.txt","w")as file:
# #         file.write(name +","+age)
# #     print("student added succesfully ")

# #     elif choice =="2":
# #         try:
# #             with open("student.txt","r") as file:
# #                 for line in file:
# #                     name , age =line.strip().split()
# #                     print("name",name)
# #                     print("age",age)
# #         except FileNotFoundError:
# #             print("file not found")

# #     else choice =="3":
# #         print("program ended ")
# #         break
# #     else:
# #         print(invalid choice)



# # All the things in one place

# while True:

#     print("\nStudent File")
#     print("1. Add student")
#     print("2. View student")
#     print("3. Exit")

#     choice = input("Enter a choice: ")

#     # Add student
#     if choice == "1":

#         name = input("Enter a name: ")
#         age = input("Enter age: ")

#         # "a" means append - add new student without deleting old data
#         with open("student.txt", "a") as file:
#             file.write(name + "," + age + "\n")

#         print("Student added successfully!")

#     # View students
#     elif choice == "2":

#         try:
#             with open("student.txt", "r") as file:

#                 for line in file:

#                     name,age = line.strip().split(",")

#                     print("Name:", name)
#                     print("Age:", age)
#                     print("----------------")

#         except FileNotFoundError:
#             print("File not found!")

#     # Exit
#     elif choice == "3":

#         print("Program ended!")
#         break

#     # Invalid choice
#     else:

#         print("Invalid choice!")




while True:

    print("\nStudent File")
    print("1. Add student")
    print("2. View student")
    print("3. Exit")

    choice = input("Enter a choice: ")

    # Add student
    if choice == "1":

        name = input("Enter name: ")
        age = input("Enter age: ")

        with open("student.txt", "a") as file:
            file.write(name + "," + age + "\n")

        print("Student added successfully!")

    # View student
    elif choice == "2":

        try:
            with open("student.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 2:
                        name = data[0]
                        age = data[1]

                        print("Name:", name)
                        print("Age:", age)
                        print("----------------")

                    else:
                        print("Invalid data:", line.strip())

        except FileNotFoundError:
            print("File not found!")

    # Exit
    elif choice == "3":

        print("Program ended!")
        break

    # Wrong choice
    else:

        print("Invalid choice!")

