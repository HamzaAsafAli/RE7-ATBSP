#! python3.5
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
# Chapter 7 – Pattern Matching with Regular Expressions

import pyperclip, re

# regex for matching phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    )''', re.VERBOSE)


# regex for matching email address
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # name
    @                      # @
    [a-zA-Z0-9.-]+      # domian name
    (\.[a-zA-Z]{2,4})   # eg .com
)''', re.VERBOSE)

# po = phoneRegex.search('(905)-734-4732')
# print(po.group())

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
# findall method is for finding matches using our earlier defined regex
for groups in phoneRegex.findall(text):
    # 1 is area code, 3 is first 3 digits, and 4 is last 4 digits
    # put a - b/w these three groups
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')