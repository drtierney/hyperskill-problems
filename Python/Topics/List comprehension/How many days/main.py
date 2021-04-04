seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
days = [n // (60 * 60 * 24) for n in seconds]
print(days)
