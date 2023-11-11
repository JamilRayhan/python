alphabet = ' abcdefghijklmnopqrstuvwxyz!?1234567890,.'
key = int(input('Input Key : '))


def ceaserEncrypt(plaintext):
    ciphertext = ''
    plaintext = plaintext.lower()
    for letter in plaintext:
        index = alphabet.find(letter)
        index = (index + key) % len(alphabet)
        ciphertext += alphabet[index]
    return ciphertext


def ceaserDecrypt(ciphertext):
    plaintext = ''

    for letter in ciphertext:
        index = alphabet.find(letter)
        index = (index - key) % len(alphabet)
        plaintext += alphabet[index]
    return plaintext


if __name__ == '__main__':
    message = input('Message : ')
    encrypted = ceaserEncrypt(message)
    print('Encrypted message is : ', encrypted)
    print('Decrypted message is : ', ceaserDecrypt(encrypted))
