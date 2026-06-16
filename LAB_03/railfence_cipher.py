import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests

class RailFenceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def validate_key(self, key, text):
        if not key:
            QMessageBox.warning(self, "Validation Error", "Key không được rỗng.")
            return False
        try:
            k = int(key)
        except ValueError:
            QMessageBox.warning(self, "Validation Error", "Key phải là số nguyên.")
            return False
        
        if k < 2:
            QMessageBox.warning(self, "Validation Error", "Key phải >= 2.")
            return False
        
        if text and k > len(text):
            QMessageBox.warning(self, "Validation Error", "Key không được lớn hơn độ dài text.")
            return False
            
        return True

    def call_api_encrypt(self):
        text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.text()
        if not self.validate_key(key, text):
            return

        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()
            if response.status_code == 200:
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
        text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.text()
        if not self.validate_key(key, text):
            return

        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()
            if response.status_code == 200:
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
    window = RailFenceApp()
    window.show()
    sys.exit(app.exec_())
