# 백준 온라인 1793번(타일링)
if __name__ == '__main__':
    n = int(input())
    d = [0, 1, 2]

    for i in range(3, n + 1):
        d.append(d[i - 1] + d[i - 2])

    print(d[n] % 10007)