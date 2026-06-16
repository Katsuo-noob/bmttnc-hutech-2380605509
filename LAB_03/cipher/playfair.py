class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def validate_key(self, key):
        if key is None or key.strip() == "":
            raise ValueError("Key không được rỗng")
        if not all(c.isalpha() or c.isspace() for c in key):
             raise ValueError("Key chỉ được chứa chữ cái A-Z hoặc a-z")

    def create_playfair_matrix(self, key):
        self.validate_key(key)
        key = key.upper().replace("J", "I")
        key = "".join(c for c in key if c.isalpha())
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = []
        for char in key + alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        letter = letter.upper().replace("J", "I")
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        raise ValueError(f"Không tìm thấy ký tự {letter}")

    def prepare_plain_text(self, plain_text):
        if plain_text is None or plain_text.strip() == "":
            raise ValueError("Plain text không được rỗng")
        plain_text = plain_text.upper().replace("J", "I")
        plain_text = ''.join(char for char in plain_text if char.isalpha())
        if plain_text == "":
            raise ValueError("Plain text không hợp lệ")
        prepared_text = ""
        i = 0
        while i < len(plain_text):
            first_char = plain_text[i]
            if i + 1 < len(plain_text):
                second_char = plain_text[i + 1]
                if first_char == second_char:
                    prepared_text += first_char + "X"
                    i += 1
                else:
                    prepared_text += first_char + second_char
                    i += 2
            else:
                prepared_text += first_char + "X"
                i += 1
        return prepared_text

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self.prepare_plain_text(plain_text)
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i + 2]
            r1, c1 = self.find_letter_coords(matrix, pair[0])
            r2, c2 = self.find_letter_coords(matrix, pair[1])
            if r1 == r2:
                encrypted_text += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                encrypted_text += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:
                encrypted_text += matrix[r1][c2] + matrix[r2][c1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = ''.join(c for c in cipher_text.upper() if c.isalpha()).replace("J", "I")
        if len(cipher_text) % 2 != 0:
            raise ValueError("Cipher text không hợp lệ (lẻ ký tự)")
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            r1, c1 = self.find_letter_coords(matrix, pair[0])
            r2, c2 = self.find_letter_coords(matrix, pair[1])
            if r1 == r2:
                decrypted_text += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                decrypted_text += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
            else:
                decrypted_text += matrix[r1][c2] + matrix[r2][c1]
        return decrypted_text
