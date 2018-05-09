import sys

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('GuiTest.ui', self)
        self.ui.show()

    @pyqtSlot()
    def add_btn_click(self):
        input_label = self.ui.input
        list_widget = self.ui.dataList
        data = str(input_label.text()).strip()

        if data:
            list_widget.addItem(data)
            input_label.clear()
        else:
            QMessageBox.warning(self, 'Message', '값을 입력하세요')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

