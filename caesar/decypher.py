
def decypher(data, key):
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ.!?,'
    decrypted_data = ""

    for letter in data:
        index = alphabet.find(letter)

        if index == -1:
            decrypted_data += letter

        else:
            new_index = index - key
            new_index %= len(alphabet)
            decrypted_data += alphabet[new_index:new_index+1]

    return decrypted_data


key = 1
original = str(input("Please add what code would you like to decypher:  "))

while key < 26:

    deciphered = decypher(original, key)
    print(f"Decipher with key# {key}: {deciphered}")

    if "the" in deciphered:
        break

    else:

        key = key+1
