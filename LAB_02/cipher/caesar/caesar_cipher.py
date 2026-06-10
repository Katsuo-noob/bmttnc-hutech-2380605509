from email.mime import text
from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        self.alphabet_len = len(self.alphabet)

    def encrypt_text(self, text: str, key: int) -> str:
        if not str(key).strip().isdigit():
            raise ValueError("Khóa phải là số nguyên từ 1 đến 25")

        key = int(key)

        if key < 1 or key > 25:
            raise ValueError("Khóa phải nằm trong khoảng từ 1 đến 25")

        encrypted_text = []

        for letter in text:
            if letter.upper() in self.alphabet:
                letter_index = self.alphabet.index(letter.upper())
                output_index = (letter_index + key) % self.alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(
                    output_letter if letter.isupper()
                    else output_letter.lower()
                )
            else:
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        if not str(key).strip().isdigit():
            raise ValueError("Khóa phải là số nguyên từ 1 đến 25")

        key = int(key)

        if key < 1 or key > 25:
            raise ValueError("Khóa phải nằm trong khoảng từ 1 đến 25")

        decrypted_text = []

        for letter in text:
            if letter.upper() in self.alphabet:
                letter_index = self.alphabet.index(letter.upper())
                output_index = (letter_index - key) % self.alphabet_len
                output_letter = self.alphabet[output_index]
                decrypted_text.append(
                    output_letter if letter.isupper()
                    else output_letter.lower()
                )
            else:
                decrypted_text.append(letter)
        return "".join(decrypted_text)

    def decrypt_text_with_validation(self, text: str, key: int) -> str:
        decrypted_text = []
        try:
            key = int(key)  # Đảm bảo key là số nguyên
            for letter in text:
                if letter.upper() in self.alphabet:
                    letter_index = self.alphabet.index(letter.upper())
                    output_index = (letter_index - key) % self.alphabet_len
                    output_letter = self.alphabet[output_index]
                    decrypted_text.append(output_letter if letter.isupper() else output_letter.lower())
                else:
                    decrypted_text.append(letter)
        except ValueError as e:
            return f"Lỗi: nhập khóa không hợp lệ. Vui lòng nhập một số nguyên. Chi tiết lỗi: {e}"
        return "".join(decrypted_text)