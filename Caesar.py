import string

def caesar_encryption(text, shift, alphabet = [string.ascii_lowercase,string.ascii_uppercase, string.punctuation]):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    shifted_alphabets = tuple(map(shift_alphabet, alphabet))
    final_alphabet = ''.join(alphabet)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

text = input("Enter text: ")
password = int(input("Enter password: "))
print(caesar_encryption(text, password))