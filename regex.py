#  regex in python

import re

# pattern for regex
pattern = r'[a-z]'
string= "Test"

# matching the pattern in the string
searching_str = re.search(pattern,string)
print(searching_str)

matching_str = re.match(pattern,string)
print(matching_str)