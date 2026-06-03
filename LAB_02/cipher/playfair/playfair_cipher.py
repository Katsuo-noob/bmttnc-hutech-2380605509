import re


class PlayFairCipher:

    def __init__(self):
        pass

    # ==========================
    # TẠO MA TRẬN PLAYFAIR
    # ==========================
    def create_playfair_matrix(self, key):

        # Ràng buộc key
        if not key or not key.strip():
            raise ValueError(
                "Key không được để trống"
            )

        if not re.fullmatch(r"[A-Za-z]+", key):
            raise ValueError(
                "Key chỉ được chứa chữ cái A-Z"
            )

        key = key.upper().replace("J", "I")

        # Loại bỏ ký tự trùng
        unique_key = ""

        for ch in key:
            if ch not in unique_key:
                unique_key += ch

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        matrix_data = list(unique_key)

        for ch in alphabet:
            if ch not in matrix_data:
                matrix_data.append(ch)

        return [
            matrix_data[i:i + 5]
            for i in range(0, 25, 5)
        ]

    # ==========================
    # TÌM TỌA ĐỘ KÝ TỰ
    # ==========================
    def find_letter_coords(self, matrix, letter):

        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col

        raise ValueError(
            f"Không tìm thấy ký tự {letter}"
        )

    # ==========================
    # CHUẨN HÓA PLAINTEXT
    # ==========================
    def prepare_plaintext(self, text):

        text = re.sub(r'[^A-Z]', '', text.upper())
        text = text.replace('J', 'I')

        result = ""
        i = 0

        while i < len(text):

            first = text[i]

            if i + 1 < len(text):

                second = text[i + 1]

                # Nếu 2 ký tự giống nhau
                if first == second:
                    result += first + "X"
                    i += 1
                else:
                    result += first + second
                    i += 2

            else:
                result += first
                i += 1

        # Nếu lẻ thì thêm X
        if len(result) % 2 != 0:
            result += "X"

        return result
    # ==========================
    # MÃ HÓA
    # ==========================
    def playfair_encrypt(self, plain_text, matrix):
        # Ràng buộc plaintext
        if not plain_text or not plain_text.strip():
            raise ValueError(
                "Plain text không được để trống"
            )
        plain_text = self.prepare_plaintext(
            plain_text
        )
        if len(plain_text) == 0:
            raise ValueError(
                "Plain text không hợp lệ"
            )
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            a = plain_text[i]
            b = plain_text[i + 1]
            row1, col1 = self.find_letter_coords(
                matrix, a
            )
            row2, col2 = self.find_letter_coords(
                matrix, b
            )
            # Cùng hàng
            if row1 == row2:
                encrypted_text += (
                    matrix[row1][(col1 + 1) % 5]
                    + matrix[row2][(col2 + 1) % 5]
                )
            # Cùng cột
            elif col1 == col2:
               encrypted_text += (
                    matrix[(row1 + 1) % 5][col1]
                    + matrix[(row2 + 1) % 5][col2]
                )
            # Hình chữ nhật
            else:
                encrypted_text += (
                    matrix[row1][col2]
                    + matrix[row2][col1]
                )
        return encrypted_text
    # ==========================
    # GIẢI MÃ
    # ==========================
    def playfair_decrypt(self, cipher_text, matrix):
        # Ràng buộc ciphertext
        if not cipher_text or not cipher_text.strip():
            raise ValueError(
                "Cipher text không được để trống"
            )
        cipher_text = re.sub(r'[^A-Z]','',cipher_text.upper())
        if len(cipher_text) == 0:
            raise ValueError(
                "Cipher text không hợp lệ"
            )
        if len(cipher_text) % 2 != 0:
            raise ValueError(
                "Cipher text phải có số ký tự chẵn"
            )
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(
                matrix, a
            )
            row2, col2 = self.find_letter_coords(
                matrix, b
            )
            # Cùng hàng
            if row1 == row2:
                decrypted_text += (
                    matrix[row1][(col1 - 1) % 5]
                    + matrix[row2][(col2 - 1) % 5]
                )
            # Cùng cột
            elif col1 == col2:
                decrypted_text += (
                    matrix[(row1 - 1) % 5][col1]
                    + matrix[(row2 - 1) % 5][col2]
                )
            # Hình chữ nhật
            else:
                decrypted_text += (
                    matrix[row1][col2]
                    + matrix[row2][col1]
                )               
            if decrypted_text.endswith("X"):
                decrypted_text = decrypted_text[:-1]
        return decrypted_text