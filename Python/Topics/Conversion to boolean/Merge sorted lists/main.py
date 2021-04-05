def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    # CHECK that "a" or "b" are not empty
    while len(a) != 0 or len(b) != 0:
        # CHECK that "b" is empty, or that "a" and "b" are not empty and compare the elements
        if len(b) == 0 or (len(a) != 0 and len(b) != 0 and a[0] < b[0]):
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    return c
