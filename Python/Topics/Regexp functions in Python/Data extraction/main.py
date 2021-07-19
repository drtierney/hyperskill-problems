import re

string = input()
# your code
pattern = "<START>(.*?)<END>"
search = re.search(pattern, string, flags=re.DOTALL)
if search:
    print(search.group(1))
