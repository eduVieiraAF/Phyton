
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Labels")
        self.setGeometry(200, 200, 520, 600)
        self.setWindowIcon(QIcon("PYQT5/python.png"))
        
                
        label = QLabel("Hello World", self)
        label.setGeometry(20, 20, 400, 150)
        label.setFont(QFont("Arial", 25))
        label.setStyleSheet(
            "color: cyan;" 
            "background-color: black;"
            "font-weight: bold;"
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: green;"
            )
        # label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignCenter)
        label.show()
        
        label2 = QLabel(self)
        label2.setGeometry(200, 200, 400, 150)
        pixmap = QPixmap("PYQT5/python.png")
        label2.setPixmap(pixmap)
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

