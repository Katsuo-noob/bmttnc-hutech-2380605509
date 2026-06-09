import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"

        payload = {
            "plain_text": self.ui.plaintext_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.ciphertext_txt.setPlainText(
                    data.get("encrypted_text", "")
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Encrypted Successfully"
                )

            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    response.text
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"

        payload = {
            "cipher_text": self.ui.ciphertext_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.plaintext_txt.setPlainText(
                    data.get("decrypted_text", "")
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Decrypted Successfully"
                )

            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    response.text
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())