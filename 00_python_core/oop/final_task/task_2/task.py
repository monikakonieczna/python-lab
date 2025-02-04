class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.lower()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        # Create the cipher alphabet
        self.cipher_alphabet = self.create_cipher_alphabet()

    def create_cipher_alphabet(self):
        # Remove duplicates from the keyword
        unique_keyword = ""
        for letter in self.keyword:
            if letter not in unique_keyword:
                unique_keyword += letter
        
        # Generate the cipher alphabet by appending the rest of the letters in order
        remaining_letters = [letter for letter in self.alphabet if letter not in unique_keyword]
        cipher_alphabet = unique_keyword + ''.join(remaining_letters)
        return cipher_alphabet

    def encode(self, plaintext):
        # Encode the plaintext
        plaintext = plaintext.lower()
        encoded_text = []
        for char in plaintext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encoded_text.append(self.cipher_alphabet[index])
            else:
                encoded_text.append(char)  # non-alphabet characters are unchanged
        return ''.join(encoded_text).capitalize()

    def decode(self, ciphertext):
        # Decode the ciphertext
        ciphertext = ciphertext.lower()
        decoded_text = []
        for char in ciphertext:
            if char in self.cipher_alphabet:
                index = self.cipher_alphabet.index(char)
                decoded_text.append(self.alphabet[index])
            else:
                decoded_text.append(char)  # non-alphabet characters are unchanged
        return ''.join(decoded_text).capitalize()


# Example usage:
cipher = Cipher("crypto")

# Encoding a message
encoded = cipher.encode("Hello world")
print(encoded)  # "Btggj vjmgp"

# Decoding a message
decoded = cipher.decode("Fjedhc dn atidsn")
print(decoded)  # "Kojima is genius"
