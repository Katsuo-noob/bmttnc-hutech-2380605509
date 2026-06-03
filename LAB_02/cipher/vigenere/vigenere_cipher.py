class VigenereCipher:

    def __init__(self):
        pass

    def encrypt_text(self, plain_text, key):
        if not plain_text or not plain_text.strip():
            raise ValueError("Plain text không được để trống")
        if not key or not key.strip():
            raise ValueError("Key không được để trống")
        if not key.isalpha():
            raise ValueError("Key chỉ được chứa chữ cái A-Z")
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord("A")
                if char.isupper():
                    encrypted_text += chr(
                        (ord(char) - ord("A") + key_shift) % 26 + ord("A")
                    )
                else:
                    encrypted_text += chr(
                        (ord(char) - ord("a") + key_shift) % 26 + ord("a")
                    )
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
    def decrypt_text(self, encrypted_text, key):
        if not encrypted_text or not encrypted_text.strip():
            raise ValueError("Cipher text không được để trống")
        if not key or not key.strip():
            raise ValueError("Key không được để trống")
        if not key.isalpha():
            raise ValueError("Key chỉ được chứa chữ cái A-Z")
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord("A")

                if char.isupper():
                    decrypted_text += chr(
                        (ord(char) - ord("A") - key_shift) % 26 + ord("A")
                    )
                else:
                    decrypted_text += chr(
                        (ord(char) - ord("a") - key_shift) % 26 + ord("a")
                    )
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
