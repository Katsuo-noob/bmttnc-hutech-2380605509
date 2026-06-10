import re


class PlayFairCipher:

    def __init__(self):
        pass

    # ==========================
    # VALIDATE KEY
    # ==========================
    def validate_key(self, key):

        if not key or not key.strip():
            raise ValueError(
                "Key không được để trống"
            )

        key = key.strip()

        if not re.fullmatch(r"[A-Za-z]+", key):
            raise ValueError(
                "Key chỉ được chứa chữ cái A-Z, không chứa số hoặc ký tự đặc biệt"
            )

        return key.upper().replace("J", "I")

    # ==========================
    # VALIDATE PLAINTEXT
    # ==========================
    def validate_plaintext(self, text):

        if not text or not text.strip():
            raise ValueError(
                "Plain text không được để trống"
            )

        if re.search(r"\d", text):
            raise ValueError(
                "Plain text không được chứa số"
            )

        if re.search(r"[^A-Za-z\s]", text):
            raise ValueError(
                "Plain text chỉ được chứa chữ cái và khoảng trắng"
            )

        return text

    # ==========================
    # VALIDATE CIPHERTEXT
    # ==========================
    def validate_ciphertext(self, text):

        if not text or not text.strip():
            raise ValueError(
                "Cipher text không được để trống"
            )

        if re.search(r"\d", text):
            raise ValueError(
                "Cipher text không được chứa số"
            )

        if re.search(r"[^A-Za-z\s]", text):
            raise ValueError(
                "Cipher text chỉ được chứa chữ cái và khoảng trắng"
            )

        cleaned = re.sub(
            r"\s+",
            "",
            text.upper()
        )

        if len(cleaned) == 0:
            raise ValueError(
                "Cipher text không hợp lệ"
            )

        if len(cleaned) % 2 != 0:
            raise ValueError(
                "Cipher text phải có số ký tự chẵn"
            )

        return cleaned.replace("J", "I")

    # ==========================
    # VALIDATE MATRIX
    # ==========================
    def validate_matrix(self, matrix):

        if len(matrix) != 5:
            raise ValueError(
                "Ma trận Playfair phải có 5 hàng"
            )

        for row in matrix:
            if len(row) != 5:
                raise ValueError(
                    "Ma trận Playfair phải là ma trận 5x5"
                )

        chars = []

        for row in matrix:
            chars.extend(row)

        if len(chars) != 25:
            raise ValueError(
                "Ma trận Playfair phải chứa 25 ký tự"
            )

        if len(set(chars)) != 25:
            raise ValueError(
                "Ma trận Playfair chứa ký tự trùng lặp"
            )

        if "J" in chars:
            raise ValueError(
                "Ma trận Playfair không được chứa ký tự J"
            )

        return True

    # ==========================
    # TẠO MA TRẬN PLAYFAIR
    # ==========================
    def create_playfair_matrix(self, key):

        key = self.validate_key(key)

        unique_key = ""

        for ch in key:
            if ch not in unique_key:
                unique_key += ch

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        matrix_data = list(unique_key)

        for ch in alphabet:
            if ch not in matrix_data:
                matrix_data.append(ch)

        matrix = [
            matrix_data[i:i + 5]
            for i in range(0, 25, 5)
        ]

        self.validate_matrix(matrix)

        return matrix

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

        text = re.sub(
            r'[^A-Z]',
            '',
            text.upper()
        )

        text = text.replace(
            'J',
            'I'
        )

        if len(text) == 0:
            raise ValueError(
                "Plain text phải chứa ít nhất một chữ cái"
            )

        result = ""
        i = 0

        while i < len(text):

            first = text[i]

            if i + 1 < len(text):

                second = text[i + 1]

                if first == second:
                    result += first + "X"
                    i += 1
                else:
                    result += first + second
                    i += 2

            else:
                result += first
                i += 1

        if len(result) % 2 != 0:
            result += "X"

        return result

    # ==========================
    # MÃ HÓA
    # ==========================
    def playfair_encrypt(
        self,
        plain_text,
        matrix
    ):

        self.validate_matrix(
            matrix
        )

        self.validate_plaintext(
            plain_text
        )

        plain_text = self.prepare_plaintext(
            plain_text
        )

        encrypted_text = ""

        for i in range(
            0,
            len(plain_text),
            2
        ):

            a = plain_text[i]
            b = plain_text[i + 1]

            row1, col1 = (
                self.find_letter_coords(
                    matrix,
                    a
                )
            )

            row2, col2 = (
                self.find_letter_coords(
                    matrix,
                    b
                )
            )

            # Cùng hàng
            if row1 == row2:

                encrypted_text += (
                    matrix[row1][
                        (col1 + 1) % 5
                    ]
                    +
                    matrix[row2][
                        (col2 + 1) % 5
                    ]
                )

            # Cùng cột
            elif col1 == col2:

                encrypted_text += (
                    matrix[
                        (row1 + 1) % 5
                    ][col1]
                    +
                    matrix[
                        (row2 + 1) % 5
                    ][col2]
                )

            # Hình chữ nhật
            else:

                encrypted_text += (
                    matrix[row1][col2]
                    +
                    matrix[row2][col1]
                )

        return encrypted_text

    # ==========================
    # GIẢI MÃ
    # ==========================
    def playfair_decrypt(
        self,
        cipher_text,
        matrix
    ):

        self.validate_matrix(
            matrix
        )

        cipher_text = (
            self.validate_ciphertext(
                cipher_text
            )
        )

        decrypted_text = ""

        for i in range(
            0,
            len(cipher_text),
            2
        ):

            a = cipher_text[i]
            b = cipher_text[i + 1]

            row1, col1 = (
                self.find_letter_coords(
                    matrix,
                    a
                )
            )

            row2, col2 = (
                self.find_letter_coords(
                    matrix,
                    b
                )
            )

            # Cùng hàng
            if row1 == row2:

                decrypted_text += (
                    matrix[row1][
                        (col1 - 1) % 5
                    ]
                    +
                    matrix[row2][
                        (col2 - 1) % 5
                    ]
                )

            # Cùng cột
            elif col1 == col2:

                decrypted_text += (
                    matrix[
                        (row1 - 1) % 5
                    ][col1]
                    +
                    matrix[
                        (row2 - 1) % 5
                    ][col2]
                )

            # Hình chữ nhật
            else:

                decrypted_text += (
                    matrix[row1][col2]
                    +
                    matrix[row2][col1]
                )

        # Xóa X đệm cuối nếu có
        if decrypted_text.endswith("X"):
            decrypted_text = (
                decrypted_text[:-1]
            )

        return decrypted_text