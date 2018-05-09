import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('DialEx.ui', self)
        self.ui.show()

    @pyqtSlot()
    def limit_value(self):
        dial = self.ui.dial
        print(dial.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec())
