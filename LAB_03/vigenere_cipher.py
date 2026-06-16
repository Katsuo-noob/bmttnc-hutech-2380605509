import sys
import os
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow


class VigenereApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(
            self.call_api_encrypt
        )

        self.ui.btn_decrypt.clicked.connect(
            self.call_api_decrypt
        )

    def validate_key(self, key, text):

        if not key:
            QMessageBox.warning(
                self,
                "Validation Error",
                "Key không được rỗng."
            )
            return False

        if not all(c.isalpha() for c in key):
            QMessageBox.warning(
                self,
                "Validation Error",
                "Key chỉ được chứa chữ cái A-Z hoặc a-z."
            )
            return False

        if not text.strip():
            QMessageBox.warning(
                self,
                "Validation Error",
                "Văn bản không được để trống."
            )
            return False

        if len(key) > len(text.strip()):
            QMessageBox.warning(
                self,
                "Validation Error",
                "Độ dài Key không được lớn hơn độ dài văn bản."
            )
            return False

        return True

    def call_api_encrypt(self):

        key = self.ui.txt_key.text()
        plain_text = self.ui.txt_plain_text.toPlainText()

        if not self.validate_key(
            key,
            plain_text
        ):
            return

        url = "http://127.0.0.1:5000/api/vigenere/encrypt"

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:

            response = requests.post(
                url,
                json=payload
            )

            data = response.json()

            if response.status_code == 200:

                result = (
                    data.get("encrypted_message")
                    or data.get("encrypted_text")
                )

                if result:

                    self.ui.txt_cipher_text.setText(
                        result
                    )

                    QMessageBox.information(
                        self,
                        "Success",
                        "Encrypted Successfully"
                    )

                else:

                    QMessageBox.critical(
                        self,
                        "Error",
                        "Phản hồi API thiếu encrypted_message"
                    )

            else:

                QMessageBox.critical(
                    self,
                    "API Error",
                    data.get(
                        "error",
                        "Error while calling API"
                    )
                )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                f"Lỗi: {str(e)}"
            )

    def call_api_decrypt(self):

        key = self.ui.txt_key.text()
        cipher_text = self.ui.txt_cipher_text.toPlainText()

        if not self.validate_key(
            key,
            cipher_text
        ):
            return

        url = "http://127.0.0.1:5000/api/vigenere/decrypt"

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:

            response = requests.post(
                url,
                json=payload
            )

            data = response.json()

            if response.status_code == 200:

                result = (
                    data.get("decrypted_message")
                    or data.get("decrypted_text")
                )

                if result:

                    self.ui.txt_plain_text.setText(
                        result
                    )

                    QMessageBox.information(
                        self,
                        "Success",
                        "Decrypted Successfully"
                    )

                else:

                    QMessageBox.critical(
                        self,
                        "Error",
                        "Phản hồi API thiếu decrypted_message"
                    )

            else:

                QMessageBox.critical(
                    self,
                    "API Error",
                    data.get(
                        "error",
                        "Error while calling API"
                    )
                )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                f"Lỗi: {str(e)}"
            )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = VigenereApp()
    window.show()

    sys.exit(app.exec_())