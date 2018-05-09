if __name__ == '__main__':
    list_a = ['a', 'b', 'c', 'd', 'e']
    list_b = list_a
    del list_a[0]

    print('list_a:{0}'.format(list_a))
    print(('list_b: {0}'.format(list_b)))

    list_c = list_a.copy()
    del list_a[0]

    print('list_a:{0}'.format(list_a))
    print('list_c: {0}'.format(list_c))
