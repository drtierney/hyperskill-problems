import re


# put your regex in the variable template
template = r"(\d{1,2}\).\w+.){1,}$"
re.escape(template)
