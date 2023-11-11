import random
import matplotlib.pylab as plt

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = random.randint(1, 10)


def ceaserEncrypt(plaintext):
    ciphertext = ''
    plaintext = plaintext.lower()
    for letter in plaintext:
        index = alphabet.find(letter)
        index = (index + key) % len(alphabet)
        ciphertext += alphabet[index]
    return ciphertext


def frequency_analysis(text):
    text = text.lower()
    letter_frequency = {
        
    }
    for letter in alphabet:
        letter_frequency[letter] = 0
    
    for letter in text:
        if letter in alphabet:
            letter_frequency[letter] += 1
    return letter_frequency


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


def ceaser_crack(text):
    freq = frequency_analysis(text)
    freq = sorted(freq.items(),key = lambda x : x[1],reverse=True)
    key=alphabet.find(freq[0][0])-alphabet.find('e')
    print(key)
    
    
if __name__ == '__main__':
    plain_text = "Consequt met dolor ex nulla culpa labore ut nostrud consequat dolore e id proident enim Adipisicing deserunt elit null ullamco magna quis ad anim nulla est nulla amet esse Est id eiusmod duis culpa minim tempor Lorem et officia pariatur anim  Ad excepteur proident ullamco magn magn laborum dolore ad officia qui et eiusmod laboris Adipisicing nostrud mollit et culp duis cillum veniam et voluptate excepteur ad ex elit"
    chipher_text = ceaserEncrypt(plain_text)
    print(chipher_text)
    ceaser_crack(chipher_text)
    
    