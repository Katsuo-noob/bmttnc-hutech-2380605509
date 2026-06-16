class VigenereCipher:
    def __init__(self):
        pass

    def validate_key(self, key):
        if key is None or key.strip() == "":
            raise ValueError("Key không được rỗng")
        if not all(c.isalpha() for c in key):
            raise ValueError("Key chỉ được chứa chữ cái A-Z hoặc a-z")

    def encrypt_text(self, plain_text, key):
        self.validate_key(key)
        encrypted_text = ""
        key = key.upper()
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt_text(self, encrypted_text, key):
        self.validate_key(key)
        decrypted_text = ""
        key = key.upper()
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
