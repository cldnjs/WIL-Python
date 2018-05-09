import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("HelloWorld.ui")
        self.ui.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    print('before')
    sys.exit(app.exec())
