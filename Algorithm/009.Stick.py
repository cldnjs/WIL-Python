# 백준 온라인 1094번 문제(막대기)
if __name__ == '__main__':
    length = 64
    x = int(input())
    count = 0

    while x > 0:
        if length > x:
            length /= 2
        else:
            x -= length
            count += 1

    print(count)
