import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
import requests

class PlayfairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def validate_key(self, key):
        if not key:
            QMessageBox.warning(self, "Validation Error", "Key không được rỗng.")
            return False
        if not all(c.isalpha() or c.isspace() for c in key):
            QMessageBox.warning(self, "Validation Error", "Key chỉ được chứa chữ cái A-Z hoặc a-z.")
            return False
        return True

    def call_api_encrypt(self):
        key = self.ui.txt_key.text()
        if not self.validate_key(key):
            return

        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()
            if response.status_code == 200:
                # Handle both possible keys for robustness
                result = data.get("encrypted_message") or data.get("encrypted_text")
                if result:
                    self.ui.txt_cipher_text.setText(result)
                    QMessageBox.information(self, "Success", "Encrypted Successfully")
                else:
                    QMessageBox.critical(self, "Error", "Phản hồi API thiếu 'encrypted_message'")
            else:
                QMessageBox.critical(self, "API Error", data.get("error", "Error while calling API"))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi: {str(e)}")

    def call_api_decrypt(self):
        key = self.ui.txt_key.text()
        if not self.validate_key(key):
            return

        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()
            if response.status_code == 200:
                # Handle both possible keys for robustness
                result = data.get("decrypted_message") or data.get("decrypted_text")
                if result:
                    self.ui.txt_plain_text.setText(result)
                    QMessageBox.information(self, "Success", "Decrypted Successfully")
                else:
                    QMessageBox.critical(self, "Error", "Phản hồi API thiếu 'decrypted_message'")
            else:
                QMessageBox.critical(self, "API Error", data.get("error", "Error while calling API"))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())
