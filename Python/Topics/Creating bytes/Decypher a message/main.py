message = input()
key = sum((int(input())).to_bytes(2, 'little'))
decoded = ''.join([chr(item + key) for item in message.encode()])
print(decoded)
