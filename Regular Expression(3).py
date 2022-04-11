import re

# 1. Verify mobile phone number: The rules for mobile phone numbers start with 1, the second digit can be 34587, and the next 9 digits can be arbitrary.
# text = "15589552242"
# result = re.match("1[34587]\d{9}",text)
# print(result.group())

# 2. Verify mailbox: The rules of the mailbox are that the name of the mailbox is composed of numbers, English characters, underscores, followed by the @ symbol, followed by the domain name.
# text = "dylanmeng1998@gmail.com"
# result = re.match("\w+@[a-z,0-9]+\.[a-z]+",text)
# print(result.group())

# 3. Verification URL: The rule is to be preceded by http or https or ftp, followed by a colon, followed by a slash, followed by any non-blank characters.
text = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
result = re.match("(http|https|ftp)://\S+",text)
print(result.group())

# 4. Verify ID card: The rule of ID card is that there are 18 digits in total, the first 17 digits are all numbers, and the last digit can be a number, a lowercase x, or an uppercase X.
text = "370681199807250015"
result = re.match("\d{17}[\dxX]",text)
print(result.group())