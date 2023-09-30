
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys

def display_message():
    msg = QMessageBox()
    msg.setWindowTitle("Message")
    msg.setText("Hello, World!")
    msg.exec()

app = QApplication(sys.argv)

window = QWidget()

button = QPushButton("Click me", window)
button.clicked.connect(display_message)


window.show()
app.exec()

window = QWidget()


