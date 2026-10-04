# craeting a file 

file = open("stu.txt","w")
 # file = open ("filename",w->write)
file.write("name : rahul\n")
# write in that 
file.write("Age:18\n")
file.write("course:python\n ")
file.write("\n welcome to python world\n ")



file.close()
# file is closed
print("file is created ")