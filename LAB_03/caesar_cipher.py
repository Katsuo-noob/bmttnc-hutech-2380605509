import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def validate_key(self, key):
        if not key:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập khóa.")
            msg.setWindowTitle("Lỗi nhập liệu")
            msg.exec_()
            return False
        try:
            key_int = int(key)
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Khóa Caesar phải là số nguyên.")
            msg.setWindowTitle("Lỗi nhập liệu")
            msg.exec_()
            return False

        # Kiểm tra khoảng hợp lệ
        if not (0 <= key_int <= 25):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Khóa Caesar phải nằm trong khoảng từ 0 đến 25.")
            msg.setWindowTitle("Lỗi nhập liệu")
            msg.exec_()
            return False

        return True

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        key = self.ui.txt_key.text()
        plain_text = self.ui.txt_plain_text.toPlainText()

        if not self.validate_key(key):
            return

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                data = response.json()
                error_msg = data.get("error", "Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(error_msg)
                msg.setWindowTitle("API Error")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Kết nối API thất bại: {str(e)}")
            msg.exec_()

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        key = self.ui.txt_key.text()
        cipher_text = self.ui.txt_cipher_text.toPlainText()

        if not self.validate_key(key):
            return

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                data = response.json()
                error_msg = data.get("error", "Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(error_msg)
                msg.setWindowTitle("API Error")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Kết nối API thất bại: {str(e)}")
            msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())