import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('MainWindow.ui')

    @pyqtSlot()
    def send_btn_click(self):
        msg = self.ui.lineEdit.text()
        print(msg)

    def show(self):
        self.ui.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
