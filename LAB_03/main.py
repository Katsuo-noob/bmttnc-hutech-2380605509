import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import os

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab 03 - Cipher Selection")
        self.setGeometry(100, 100, 300, 150)
        
        layout = QVBoxLayout()
        
        label = QLabel("LAB 03 - CIPHERS")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(label)
        
        btn_caesar = QPushButton("Caesar Cipher")
        btn_caesar.clicked.connect(lambda: self.launch("caesar_cipher.py"))
        layout.addWidget(btn_caesar)
        
        btn_vigenere = QPushButton("Vigenere Cipher")
        btn_vigenere.clicked.connect(lambda: self.launch("vigenere_cipher.py"))
        layout.addWidget(btn_vigenere)
        
        btn_railfence = QPushButton("Rail Fence Cipher")
        btn_railfence.clicked.connect(lambda: self.launch("railfence_cipher.py"))
        layout.addWidget(btn_railfence)
        
        btn_playfair = QPushButton("Playfair Cipher")
        btn_playfair.clicked.connect(lambda: self.launch("playfair_cipher.py"))
        layout.addWidget(btn_playfair)
        
        self.setLayout(layout)

    def launch(self, filename):
        # Run the script in a new process so it doesn't block
        os.system(f"start py {filename}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())
