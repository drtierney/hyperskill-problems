import re 

string = input()
dates = re.compile(r'''
                   ^(0[1-9]|[12][0-9]|3[01])     # digits from 01 to 31
                   (/)                           # forward slash 
                   (0[1-9]|1[012])               # digits from 01 to 12
                   (/)                           # forward slash
                   (19|20)\d\d$                  # 19 or 20 with any two digits
                   ''', flags=re.VERBOSE)
result = dates.match(string)
print(result)
