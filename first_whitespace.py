# Search for the first white-space character in the string:

import re 

str1 = "Hello world,Hi goodmorning"
res3 = re.search("\s",str1)
print(res3)
print("The first white-space character is located in position:", res3.start())
