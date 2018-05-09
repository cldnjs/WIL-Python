import random
import socket
import sys

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

import os


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('FileBrowseEx.ui', self)
        self.ui.show()

    @pyqtSlot()
    def browse_btn_click(self):
        file_path = self.open_file_browser()
        self.ui.fileName.setText(file_path)

    @pyqtSlot()
    def upload_btn_click(self):
        BUFFER_SIZE = 8 * 1024
        file_path = self.ui.fileName.text()
        file_name = os.path.splitext(os.path.basename(file_path))
        send_file_name = file_name[0] + '({0})'.format(random.randint(1, 1000)) + file_name[1]
        send_size = 0

        if not os.path.isfile(file_path):
            print('파일이 존재하지 않습니다.')
            return

        with socket.socket() as sock:
            sock.connect((socket.gethostname(), 1004))
            sock.send(send_file_name.encode('utf-8'))

            print('[파일 전송 시작]')
            with open(file_path, 'rb') as f:
                data = f.read(BUFFER_SIZE)
                while data:
                    send_size += len(data)
                    sock.send(data)
                    data = f.read(BUFFER_SIZE)
            print('[파일 전송 완료({0} 바이트)]\n'.format(send_size))
            sock.close()

    def open_file_browser(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, '파일 열기')
        return file


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
