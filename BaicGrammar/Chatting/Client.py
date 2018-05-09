import socket

if __name__ == '__main__':
    s = socket.socket()
    host = socket.gethostname()
    port = 9009

    s.connect((host, port))
    print('Connection established: {0}'.format(host))

    while True:
        send_data = input('Enter something for Server: ')
        s.send(send_data.encode())

        print('[Waiting for response]')
        print(s.recv(1024).decode('utf-8'))

