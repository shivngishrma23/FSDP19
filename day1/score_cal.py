a1 = int(input("enter marks for assignment 1: "))
a2 = int(input("enter marks for assignment 2: "))
a3 = int(input("enter marks for assignment 3: "))

e1 = int(input("enter the marks for exam1 : "))
e2 = int(input("enter the marks for exam2 : "))

weighted_score = (a1+a2+a3) * 0.1 + (e1+e2)*0.35
print("weighted score is " + str(weighted_score))