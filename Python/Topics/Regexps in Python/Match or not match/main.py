import re


def matched(template, string):
    if re.match(template, string):
        return True
    return False
