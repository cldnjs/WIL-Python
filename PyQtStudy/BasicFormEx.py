import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('BasicFormEx.ui', self)
        self.ui.show()

    @pyqtSlot()
    def first_btn_click(self):
        print()
        self.ui.resultLabel.setText("첫번째 버튼")

    @pyqtSlot()
    def second_btn_click(self):
        self.ui.resultLabel.setText("두번째 버튼")

    @pyqtSlot()
    def third_btn_click(self):
        self.ui.resultLabel.setText("세번째 버튼")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
