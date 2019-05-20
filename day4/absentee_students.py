
#file Handling
file = open('absent_students.txt','w')
file.close()

with open('absent_students.txt','a') as file:
    for i in range(25):
        absent_student_name = input("Enter the absent student name: ")
        if absent_student_name=="":
            break
        file.write(absent_student_name+'\n')
        

file = open('absent_students.txt','r')
print (file.readlines())
    