#copying one file to another
another_file = open('abc.txt','wt')
with open('words.txt','rt') as file:
    for text in file.readlines():
        another_file.write(text)
another_file.close()