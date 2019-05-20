#card number
import re

reg = r'^[456](\d{15}|\d{3}-(\d{4}-){2}\d{4})$'

while True:
    a = input().strip()
    if not a:
        break
    chk = re.match(reg,a)
    rep = re.search(r'(\d)\1{3,}',a.replace('-',''))
    if chk and not rep:
        print ("Valid")
    else:
        print ("Invalid")
