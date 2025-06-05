import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QCheckBox
from PyQt6.QtWidgets import QLabel, QLineEdit, QMainWindow


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 400, 250, 250)
        self.setWindowTitle('Музыкальные стили')
        self.reggae = QCheckBox('reggae', self)
        self.reggae.resize(60, 60)
        self.reggae.move(20, 40)
        self.jazz = QCheckBox('jazz', self)
        self.jazz.resize(60, 60)
        self.jazz.move(20, 60)
        self.folk = QCheckBox('folk', self)
        self.folk.resize(60, 60)
        self.folk.move(20, 80)
        self.blues = QCheckBox('blues', self)
        self.blues.resize(60, 60)
        self.blues.move(20, 100)

        self.blues.clicked.connect(self.check_blues)

    def check_blues(self):
        if self.blues.checkState() == Qt.Checked:
            self.LabelBlues = QLabel('Блюз')
            self.move(40, 100)

    def reggae1(self):
        if self.reggae.setChecked(True):
            self.LabelRegg = QLabel('РЕГГИ')
            self.move(40, 40)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
