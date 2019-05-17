u_input= input("enter nubers:").split()
input_length= len(u_input)
count = 0
palindromic_integer = False
for num in u_input:
    if int(num)>0:
        count +=1
       
if count == input_length:        
        for positivenum in u_input:
            if positivenum == positivenum[::-1]:
                palindromic_integer = True
print(palindromic_integer)                
#_____________________________________ ANOTHER LOGIC_______________________________________
u_input= input("enter nubers:").split()
if all([int(i)>0 for i in u_input]) and any([i==i[::-1]for i in u_input]):
    print("True")
else:
    print("False")
               