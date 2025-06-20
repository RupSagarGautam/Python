#  regex in python

import re

# # pattern for regex
# pattern = r'[a-z]'
# string= "Test"

# # searching the pattern in the string
# if re.search(pattern,string):
#     print("searching_str")

# # matching the paggern in str
# if re.match(pattern,string):
#     print("matching_str")
    
# pattern = r'[A-Z]+[a-z]+\d'
# string = input("Enter String")

# if re.match(pattern,string):
#     print("Pattern Matched")
# else:
#     print("Pattern not matched")
    
pattern = r'[A-Za-z0-9]/+@[A-Za-z]+/.com'
string = input("Enter Your Email: ")

if re.match(pattern,string):
    print("Valid Email")

else:
    print("Invalid Email")