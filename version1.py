import random
originalKey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(),./?;:+-_='


def encrypt(text):
    if len(text)>9:
        pos = random.randint(1, 9)
    else:
        pos = random.randint(0, len(text)-1)
    
    rand = random.randint(1, 9)
    IV = random.randint(10**(rand-1), 10**rand-1)

    if IV % len(originalKey) == 0:
        IV = IV + 3
    key = originalKey*(IV // len(originalKey) + 1)

    value = ''
    position = 0
    for char in originalKey:
        if char in originalKey:
            index = originalKey.index(char)
            position = (index + IV) % len(originalKey)

        value += key[position]

    encrypted_text = ''
    for char in text:
        if char in key:
            index = key.index(char)
            encrypted_text += value[index]
        else:
            encrypted_text += char
    returntext = str(pos)  + encrypted_text[:pos] + str(rand) + str(IV) + encrypted_text[pos:]

    return returntext

def decrypt(text):
    pos = int(text[:1])
    text = text[1:]
    rand = int(text[pos:pos+1])
    IV = int(text[pos+1:pos+1+rand])
    text = text[:pos] + text[pos+1+rand:]

    if IV % len(originalKey) == 0:
        IV = IV + 3
    key = originalKey*(IV // len(originalKey) + 1)

    value = ''
    position = 0
    for char in originalKey:
        if char in originalKey:
            index = originalKey.index(char)
            position = (index + IV) % len(originalKey)

        value += key[position]

    decrypted_text = ''
    for char in text:
        if char in value:
            index = value.index(char)
            decrypted_text += key[index]
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    sample_text = "hello"
    encrypted = encrypt(sample_text)
    print(f"Original: {sample_text}")
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt("encrypted")

    
    print(f"Decrypted: {decrypted}")