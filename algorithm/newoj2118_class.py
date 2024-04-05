import re

pat = re.compile(r'\d*'.join('2023'))
nums = range(12345678, 98765432 + 1)
print(sum(not re.search(pat, i) for i in map(str, nums)))
