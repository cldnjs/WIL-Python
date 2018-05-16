# 백준 온라인 1475번 문제
import math


if __name__ == '__main__':
    n = input()
    list_a = list(int(n[i]) for i in range(len(n)))

    cnt = [0] * 10

    for i in range(len(list_a)):
        if not(list_a[i] == 6) and not(list_a[i] == 9):
            cnt[list_a[i]] += 1
        else:
            cnt[6] += 0.5

    print(math.ceil(max(cnt)))
