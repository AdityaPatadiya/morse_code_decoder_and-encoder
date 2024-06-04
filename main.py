morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}


def encrypt(text):
    encrypted_text = ''
    for letter in text:
        if letter != ' ':
            encrypted_text += morse_code[letter.upper()] + ' '
        else:
            encrypted_text += ' '
    return encrypted_text


def decrypt(text):
    decrypted_text = ''

    key_list = list(morse_code.keys())
    value_list = list(morse_code.values())

    morse_code_list = text.split(' ')
    for letter in morse_code_list:
        if letter in value_list:
            decrypted_text += key_list[value_list.index(letter)]
        else:
            decrypted_text += ' '
    return decrypted_text


user_input = input("What would you like to encrypt or decrypt? ")
if user_input == 'encrypt':
    string = input("Enter the string you want to encrypt: ")
    result = encrypt(string)
    print(result)

elif user_input == 'decrypt':
    string = input("Enter the string you want to decrypt: ")
    result = decrypt(string)
    print(result)

else:
    print("Invalid input. Please try again.")
