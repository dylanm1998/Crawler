import re

# *: Match zero or more characters
text = "+abc"
result = re.match('\D*',text)
print(result.group())

# +: Match one or more characters
text = "1abc"
result = re.match('\w+',text)
print(result.group())

# ?: Match 0 or 1 of the previous character:
text = "1abc"
result = re.match('\w?',text)
print(result.group())

# {m}: Match m characters：
text = "1abc"
result = re.match('\w{2}',text)
print(result.group())

# {m,n}: Match the number of characters between m-n
text = "1abc"
result = re.match('\w{1,3}',text)
print(result.group())