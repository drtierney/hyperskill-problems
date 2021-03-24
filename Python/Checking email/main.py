def check_email(string):
    return " " not in string and "@" in string and "@." not in string \
           and string.rfind(".", string.find("@")) != -1
