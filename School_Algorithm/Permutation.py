def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


if __name__ == '__main__':
    str_a = 'a'
    str_b = 'b'
    data_list = list()

    a, b, c = map(int, input().split())
    for i in range(a):
        data_list.append(str_a)
    for j in range(b):
        data_list.append(str_b)

    my_permutation = permutations(data_list)
    my_permutation = list(set(my_permutation))
    my_permutation.sort()

    for data in my_permutation[c - 1]:
        if data == 'a':
            print('-', end=' ')
        elif data == 'b':
            print('o', end=' ')
