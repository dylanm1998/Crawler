import re

# Escape character in python:
# raw
text = r"hello\nworld"
print(text)

# Escape characters in regular expressions:
text = "apple price is $99, orange price is $88"
result = re.findall("\$\d+",text)
print(result)

# Native string and regular exxpression:
# String parsing rules for regular expressions:
# 1. First put this string in the Python language level for parsing
# 2. Put the result of parsing at the Python language level and then parse it at the regular expression level
text = "\cba c"
result = re.match("\\\\c",text) # \\\\c =(Python language level)> \\c =(Regular expression level)> \c
print(result.group())

text = "\cba c"
result = re.match(r"\\c",text) # \\c =(Regular expression level)> \c
print(result.group())