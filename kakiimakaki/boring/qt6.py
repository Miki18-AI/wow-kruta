import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber
from PyQt6.QtWidgets import QLabel, QLineEdit, QMainWindow


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.music = 0
        self.playlist = ['dsf - gfd', 'scdfa - gfds', 'павпвапавп - fdsflhjkadgre']

    def initUI(self):
        self.setGeometry(700, 400, 250, 250)
        self.setWindowTitle('PyQT6 ypok 2')
        self.login = QLabel('Воспроизведение остановдено ', self)
        self.login.move(50, 50)
        self.password = QLabel('павпвапавп', self)
        self.password.move(90, 100)
        self.btn01 = QPushButton('Play', self)
        self.btn02 = QPushButton('>|', self)
        self.btn03 = QPushButton('|<', self)
        self.btn01.resize(40, 25)
        self.btn01.move(100, 150)
        self.btn02.resize(40, 25)
        self.btn02.move(140, 150)
        self.btn03.resize(40, 25)
        self.btn03.move(60, 150)
        self.traeck_info = QLCDNumber(self)
        self.traeck_info.move(100, 20)
        self.btn01.clicked.connect(self.clickbut)
        self.btn02.clicked.connect(self.clickright)
        self.btn03.clicked.connect(self.clickleft)

    def clickbut(self):
        if self.btn01.text() == 'Play':
            self.btn01.setText('Pause')
            self.login.setText('Сейчас играет')
        else:
            self.btn01.setText('Play')
            self.login.setText('Воспроизведение остановдено ')

    def clickright(self):
        self.music += 1
        if self.music == len(self.playlist):
            self.music = 0
        self.password.setText(self.playlist[self.music])
        self.traeck_info.display(self.music + 1)

    def clickleft(self):
        self.music -= 1
        if self.music < 0:
            self.music = len(self.playlist) - 1
        self.password.setText(self.playlist[self.music])
        self.traeck_info.display(1 + self.music)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
