
def encoding(data, key):
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ.!?,'
    encrypted_data = ""

    for letter in data:
        index = alphabet.find(letter)

        if index == -1:
            encrypted_data += letter

        else:
            new_index = index + key
            new_index %= len(alphabet)
            encrypted_data += alphabet[new_index:new_index+1]

    return encrypted_data


key = int(input("Please add a cypher key:  "))
original = str(input("Please add the message you want to encrypt:  "))
print('Original:', original)
ciphered = encoding(original, key)
print('  Cipher:', ciphered)
