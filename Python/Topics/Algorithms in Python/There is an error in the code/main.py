sentence = input()


def aver(sent):

    for sym in ['!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()

    total = 0
    for word in words:
        total = total + len(word)

    if words:
        return total / len(words)
    return 0


print(aver(sentence))
