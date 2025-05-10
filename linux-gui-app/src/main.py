import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Toggle App")
        self.setGeometry(100, 100, 400, 300)
        self.button = QPushButton("Toggle Color", self)
        self.button.clicked.connect(self.toggle_color)
        self.button.setGeometry(150, 130, 100, 40)
        self.is_blue = True
        self.setStyleSheet("background-color: blue;")

    def toggle_color(self):
        if self.is_blue:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("background-color: blue;")
        self.is_blue = not self.is_blue

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())