import random
originalKey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(),./?;:+-_= '

text= "Hello world!"
pin = 1234

def encrypt(text):
    chars = len(text)
    maxlimit = 10**chars -1
    minlimit = 10**(chars-1)

    if chars>9:
        pos = random.randint(0, 9)
    else:
        pos = random.randint(0, len(text)-1)

    rand = random.randint(minlimit, maxlimit)
    
    IV = str(rand)

    i = 0
    encryption = ""
    while i != len(IV):
        j = text[i]
        k= IV[i]
        index = originalKey.index(j)
        position = (index + int(k))% len(originalKey)
        encryption = encryption + originalKey[position]
        i += 1
    returntext = str(pos)  + encryption[:pos] + str(int(IV)+pin) + encryption[pos:]
    return returntext


def decrypt(encrypted_text):
    pos = int(encrypted_text[:1])
    encrypted_text = encrypted_text[1:]
    
    IV = int(encrypted_text[pos:pos+len(encrypted_text)//2]) - pin
    IV = str(IV)
    cipher_text = encrypted_text[:pos] + encrypted_text[pos+len(IV):]

    i = 0
    decryption = ""
    
    while i != len(IV):
        j = cipher_text[i]
        k = IV[i]
        index = originalKey.index(j)
        position = (index - int(k)) % len(originalKey)
        decryption = decryption + originalKey[position]
        i += 1
    return decryption

entc = encrypt(text)
print("Encrypted Text:", entc)
print("Decrypted Text:", decrypt(entc))
