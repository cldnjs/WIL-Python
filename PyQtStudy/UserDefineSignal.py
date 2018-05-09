import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TicGenerator(QThread):
    tic = pyqtSignal(name="Tic")

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            t = int(time.time())
            if not t % 5 == 0:
                self.usleep(1)
                continue
            self.Tic.emit()
            self.msleep(1000)


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('UserDefineSignal.ui', self)
        self.setWindowTitle('사용자 정의 시그널')
        self.tic_gen = TicGenerator()
        self.init_widget()

    def init_widget(self):
        self.tic_gen.Tic.connect(
            lambda: self.textEdit.insertPlainText(time.strftime("[%H:%M:%S] Tic!\n"))
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    form.tic_gen.start()
    sys.exit(app.exec())
