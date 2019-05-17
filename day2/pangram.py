input_string = input("enter any string : ")
count= 0
list1= []
lower = input_string.lower()
for alpha in  list1:
    list1.append(alpha)
    
final_list = []
for num in list1:
     if num not in final_list:
         final_list.append(num)
         
for elements in final_list:
    if elements in 'abcdefghijklmnopqrstuvwxyz':
        count +=1
       
if count == 26:
    print("PANGRAM")
else:
    print("NOT PANGRAM")
       
        