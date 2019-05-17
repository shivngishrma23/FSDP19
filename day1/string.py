name = input("enter your name with lastname : ")
space_index = name.index(' ')
print(name[space_index+1:]+' '+name[0:space_index+1])
