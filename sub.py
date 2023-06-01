# The sub() function replaces the matches with the text of your choice:

import re 

str3 = "Boby has a blue eyes"
res6 = re.sub("\s","Q",str3)
print(res6)


str4 = "Boby has a blue eyes"
res7 = re.sub("\s","*",str4,2)
print(res7)
