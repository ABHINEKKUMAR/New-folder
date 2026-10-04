# try:
#     # code that may casue  an error 
# except:
#     # code that runs if error occurs 


try:
    a=10
    b=20
    print(a/b)

except:
    print("something is wromng")



try:
    age=int(input("eneter a age"))
    print("age",age)

except ValueError:
    print("please eneter a vaild number only")


try:
    a=int(input("enter a first no"))
    b=int(input("enter a second no"))

    result = a/b

except ZeroDivisionError:
    print("cannot divided by zero")

except ValueError:
    print("eneter number only")

else:
    print("result",result)



# try except  else   finally run  