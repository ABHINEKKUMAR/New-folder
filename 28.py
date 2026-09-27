def geet(name="Student"):
 print("hello",name)

geet("Rahul")
geet()



# local and global 

# global 
x=100

def show():
    y =20  # local value
    print(x)
    print(y)


show()
print(x)
