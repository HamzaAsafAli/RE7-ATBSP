#! python3.5
# PasswordDetector.py - Determine password strength

import re

# mediumPass = re.compile(r'[A-Za-z0-9@#$%^&+=]{5,}')
#
# strongPass = re.compile(r'.*\W.*')


# po = mediumPass.search('12a45')
# print(po)
# print(po.group())

# so = strongPass.search('hello%jisbs')
# print(so)
# print(so.group())

password = input("Enter desired password: ")
# a strong password needs at least one symbol 
if (len(password) >= 8) and (re.match(r'.*\W.*', password)):
    print("Strong password")
elif (len(password) >= 5) and (re.match(r'[A-Za-z0-9@#$%^&+=]', password)):
    print("Medium password")
else:
    print("Weak Password")




