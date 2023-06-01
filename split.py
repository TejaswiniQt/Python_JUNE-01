# split() function

import re 

str2 = "Boby has a blue eyes"
res4 = re.split("\s",str2)
print(res4)

# Split the string only at the first occurrence:

str3 = "Boby has a blue eyes"
res5 = re.split("\s",str3,1)
print(res5)

