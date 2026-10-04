file = open("student.txt",'r')

print(file.readline())

print(file.readline())

print(file.readline())

print(file.readline())
file.close()




# for loop 

file = open("student.txt",'r')

for line in file:
    print(line.strip())
file.close()