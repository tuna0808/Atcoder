import re
s = input()

m = re.search(r'\d+', s)

print(m.group())
