import re

# ^: To... beginning:
text = "hello world"
result = re.search("^hello",text)
#result = re.match("hello ",text)
print(result.group())

# $: To... ending:
text = "hello world"
result = re.search("world$",text)
#result = re.match("hello ",text)
print(result.group())

text = ""
result = re.search("^$",text)
#result = re.match("hello ",text)
print(result.group())


# |: Match multiple strings or expressions:


# Greedy(+) and non-greedy(+?):
text = "12345"
result = re.search("\d+?",text)
print(result.group())

# Case 1: Extract html tag name
text = "<h1>title</h1>"
result = re.search("<.+?>",text)
print(result.group())

# Case 2: Verify that a character is a number between 0-100:
# 0,1,99,100
# 01
text = "99"
result = re.match("0$|[1-9]\d?$|100$",text)
print(result.group())