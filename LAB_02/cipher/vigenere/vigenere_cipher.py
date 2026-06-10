import re


class VigenereCipher:

    def __init__(self):
        pass

    # ==========================
    # VALIDATE KEY
    # ==========================
    def validate_key(self, key):

        if not key or not key.strip():
            raise ValueError("Key không được để trống")

        key = key.strip()

        if not re.fullmatch(r"[A-Za-z]+", key):
            raise ValueError(
                "Key chỉ được chứa chữ cái A-Z, không số, không ký tự đặc biệt"
            )

        return key.upper()

    # ==========================
    # VALIDATE PLAINTEXT
    # ==========================
    def validate_plaintext(self, text):

        if not text or not text.strip():
            raise ValueError("Plain text không được để trống")

        text = text.strip()

        # Cho phép cả chữ hoa và chữ thường
        if not re.fullmatch(r"[A-Za-z]+", text):
            raise ValueError("Plain text chỉ được chứa chữ cái A-Z hoặc a-z, không số, không ký tự đặc biệt, không dấu")

        return text

    # ==========================
    # VALIDATE CIPHERTEXT
    # ==========================
    def validate_ciphertext(self, text):

        if not text or not text.strip():
            raise ValueError("Cipher text không được để trống")

        return text

    # ==========================
    # MÃ HÓA
    # ==========================
    def encrypt_text(self, plain_text, key):

        plain_text = self.validate_plaintext(plain_text)
        key = self.validate_key(key)

        encrypted_text = ""
        key_index = 0

        for char in plain_text:

            if char.isalpha():

                key_shift = ord(key[key_index % len(key)]) - ord("A")

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
                # giữ nguyên số, dấu cách, ký tự đặc biệt
                encrypted_text += char

        return encrypted_text

    # ==========================
    # GIẢI MÃ
    # ==========================
    def decrypt_text(self, encrypted_text, key):

        encrypted_text = self.validate_ciphertext(encrypted_text)
        key = self.validate_key(key)

        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:

            if char.isalpha():

                key_shift = ord(key[key_index % len(key)]) - ord("A")

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