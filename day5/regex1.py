#floating point or not

import re

string_N = input("Enter floating point number : ")

match_obj = re.match(r"[-+]?\d*\.\d+$",string_N)

if match_obj:
    print ("True")
    
else:
    print ("False")