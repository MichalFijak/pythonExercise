import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("icons8-small-50.jpg"))

        label = QLabel("Hello, World!", self)
        label.setFont(QFont("Arial", 24))
        label.setStyleSheet("color: black;")
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: #13366e;""background-color: #a2b3ad;""font-weight: bold;""font-size: 20px;""border-radius: 10px;")
        label.setAlignment(Qt.AlignCenter)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()