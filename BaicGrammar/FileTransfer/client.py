import socket
import os


if __name__ == '__main__':
    BUFFER_SIZE = 8 * 1024
    host = socket.gethostname()
    port = 1004
    send_size = 0

    with socket.socket() as sock:
        sock.connect((host, port))
        send_file = 'test.txt'

        if not os.path.isfile(send_file):
            print('파일 존재하지않음')

        print('[파일 전송 시작]')
        with open(send_file, 'rb') as f:
            data = f.read(BUFFER_SIZE)
            while data:
                send_size += len(data)
                sock.send(data)
                data = f.read(BUFFER_SIZE)
        print('[파일 전송 완료({0} 바이트)]'.format(send_size))

    sock.close()
