# use the function blackbox(lst) that is already defined
lst = ["a", "b", "c"]
blackbox_lst = blackbox(lst)

print("modifies" if id(lst) == id(blackbox_lst) else "new")
