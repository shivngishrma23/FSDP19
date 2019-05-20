
import re

email_address = input("Enter your email address : ")

match_obj = re.findall(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,4}\b$",email_address)

print (match_obj)