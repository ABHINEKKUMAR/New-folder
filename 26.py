def calculate(a,b,operation):
#  function create -def  calculate -> is function name  (parameter  which we required )

     if operation == "add":
        return a+b
     elif operation == "sub":
        return a-b
     else:
        return "invalid operation"

answer = calculate(2,3,"add")  # function calling
answer2 = calculate(2,3,"sub")  

print(answer)
print(answer2)


# boolen either true or false 

def calculate(a,b,is_addition =True):
#  function create -def  calculate -> is function name  (parameter  which we required )
     if is_addition:
       return a+b
     else:
       return a-b

answer = calculate(2,3,is_addition =True)
answer2 =calculate(5,3,is_addition =False)
print(answer)
print(answer2)