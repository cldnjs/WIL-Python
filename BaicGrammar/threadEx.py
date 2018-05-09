from threading import Thread


def print_something(a):
    print('{0} 실행함'.format(a))


if __name__ == '__main__':
    t1 = Thread(target=print_something, args='hello')

    t1.start()
    t1.join()
