input_string = input("enter a string : ")
replaced_char = input("enter the chracter which you want to replace : ")
replacement_char = input("enter char you want to replace : ")

first_occurence = input_string.find(replaced_char)

print(input_string[:first_occurence+1] + input_string[first_occurence+1:].replace(replaced_char,replacement_char,1))
