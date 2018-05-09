import socketserver
from os.path import exists

HOST = ''
PORT = 9009


class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[{0}] 연결됨'.format(self.client_address[0]))
        file_name = self.request.recv(1024)
        file_name = file_name.decode('utf-8')
        download_url = 'C:\\Users\\JCW\\Downloads\\'

        data = self.request.recv(1024)
        if not data:
            print('파일[{0}]: 전송중 오류발생'.format(file_name))
            return

        with open(download_url + file_name, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = self.request.recv(1024)
            except Exception as e:
                print(e)

        print('파일[{0}] 전송종료. 전송량 [{1}]'.format(file_name, data_transferred))


def run_server():
    print('++++++파일 서버를 시작++++++')
    print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요.")

    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++파일 서버를 종료합니다.++++++')


if __name__ == '__main__':
    run_server()
