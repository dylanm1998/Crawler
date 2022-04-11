import re
# Match a string
text = "abc"
#ret = re.match('b',text)
ret = re.search('b',text)
print(ret.group())

# Dot (.): Match any character (except'\n'):
text = "+bc"
ret = re.match('.',text)
print(ret.group())

# \d: match any number
text = "123"
ret = re.match('\d',text)
print(ret.group())

# \D: match any non-digit
text = "abc"
ret = re.match('\D',text)
print(ret.group())

# \s: Matches whitespace characters (including: \n,\t,\r and spaces)
text = " bc"
print("="*30)
ret = re.match('\s',text)
print(ret.group())
print("="*30)


# \S: Non-whitespace character
text = "bc"
print("="*30)
ret = re.match('\S',text)
print(ret.group())
print("="*30)

# \w: Match a-z and A-Z as well as numbers and underscores:
text = "_bc"
print("="*30)
ret = re.match('\w',text)
print(ret.group())
print("="*30)

# \W: The match is the opposite of \w
text = "+bc"
print("="*30)
ret = re.match('\W',text)
print(ret.group())
print("="*30)

# The method of [] combinationas long as one of the dou in the brackets is satisfied, the matching is successful:
text = "bc"
print("="*30)
ret = re.match('[1b]',text)
print(ret.group())
print("="*30)

# Use the combined method to achieve[0-9]\d:
text = "123"
print("="*30)
ret = re.match('[0-9]',text)
print(ret.group())
print("="*30)

text = "678"
print("="*30)
ret = re.match('[^0-5]',text)
print(ret.group())
print("="*30)

# Use the combined method to achieve\w:
