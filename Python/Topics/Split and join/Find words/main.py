words = input().split()
end_s = [word for word in words if word.endswith("s")]
print("_".join(end_s))
