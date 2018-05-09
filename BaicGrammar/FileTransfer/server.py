import socket


if __name__ == '__main__':
    BUFFER_SIZE = 8 * 1024
    port = 1004
    sock = socket.socket()
    host = socket.gethostname()
    download_url = 'C:\\Users\\JCW\\Downloads\\'
    recv_size = 0

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)

    while True:
        print('[대기중]')
        client, address = sock.accept()
        print('연결됨[{0}]'.format(address[0]))

        file_name = client.recv(BUFFER_SIZE).decode('utf-8')

        data = client.recv(BUFFER_SIZE)
        if not data:
            print('+++++다운로드 중 오류 발생+++++')
            break

        print('[다운로드 시작]')
        with open(download_url + file_name, 'wb') as f:
            while data:
                recv_size += len(data)
                f.write(data)
                data = client.recv(BUFFER_SIZE)

        print('[다운로드 완료({0} 바이트)\n'.format(recv_size))
        client.close()
