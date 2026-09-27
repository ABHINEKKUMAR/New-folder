def greet(name="Student"):
    print("hello", name)

greet()  # default parameter 

greet("Avi") #define and declare 



def calculate(a,b):
    add = a+b
    sub = a-b
    mult= a*b

    return add, sub, mult

answer = calculate(20,10)

print(answer)

# if else loop 
def check(number):
    if number >0:
        return "postive"
    elif number <0:
        return "negative"
    else:
       return "zero"

print(check(10)) 
print(check(-10)) 
print(check(0)) 

# for loop 
for i in range (1,51):
    print(i)

def greet(n):
    for i in range(1,n+1):
        print(i)
greet(5)