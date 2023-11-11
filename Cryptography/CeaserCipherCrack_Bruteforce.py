import random

alphabet = ' abcdefghijklmnopqrstuvwxyz!?1234567890,.'
key = random.randint(1, 20)


def ceaserEncrypt(plaintext):
    ciphertext = ''
    plaintext = plaintext.lower()
    for letter in plaintext:
        index = alphabet.find(letter)
        index = (index + key) % len(alphabet)
        ciphertext += alphabet[index]
    return ciphertext


def ceaserCrack(ciphertext):
    for KEY in range(len(alphabet)):
        plaintext = ''
        for letter in ciphertext:
            index = alphabet.find(letter)
            index = (index - KEY) % len(alphabet)
            plaintext += alphabet[index]
        print("Key is : %s , the result is : %s" % (KEY, plaintext))


if __name__ == '__main__':
    message = input('Message : ')
    encrypted = ceaserEncrypt(message)
    print('Encrypted message is : ', encrypted)
    ceaserCrack(encrypted)
