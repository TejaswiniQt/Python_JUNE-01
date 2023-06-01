# Print the position (start- and end-position) of the first match occurrence.

import re 

str5 = "Boby ha s blue eyes"
res8 = re.search(r"\be\w+",str5)
print(res8.span())


str6 = "Boby ha s blue eyes"
res9 = re.search(r"\be\w+",str6)
print(res8.string)


str7 = "Boby ha s blue eyes"
res10 = re.search(r"\be\w+",str7)
print(res8.group())
