import re

w1 = input()
w2 = input()
if re.match(w1, w2):
    print(len(w1) * 2)
else:
    print('no matching')
