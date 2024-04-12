class VigenereCipher:
    def __init__(self) :
        pass
    
    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char)- ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char)- ord('a') + key_shift) % 26 + ord('a'))    
                    key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
    
    def vigenere_decrypt(self, encryted_text, key):
        decryted_text = ""
        key_index = 0
        for char in encryted_text:
            if char.isalpha():
                key_shift = ord (key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decryted_text += chr((ord(char)- ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decryted_text += chr((ord(char)- ord('a') - key_shift) % 26 + ord('a'))    
                    key_index += 1
            else:
                decryted_text += char
        return decryted_text