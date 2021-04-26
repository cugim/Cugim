import hashlib
text = input('Escreve o texo que quer criptografar: ')
hashed_output = hashlib.sha256(text.encode('ascii')).hexdigest()

print(hashed_output)