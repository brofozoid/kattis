import sys
# import re

line = input().split("-")
result = ""
for word in line:
    result += word[0]

print(result)
# print(re.findall('[A-Z][^A-Z]*', names))
