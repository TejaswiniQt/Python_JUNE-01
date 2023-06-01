# findall()

import re

msg = "Hi all,Goodmorning. Hello"
res = re.findall('Hi',msg)
print(res)

res1 = re.findall("[a-f]",msg)
print(res1)

res2 = re.findall('Welcome',msg)
print(res2)