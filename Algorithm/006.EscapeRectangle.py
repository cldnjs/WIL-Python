# 백준 온라인 1085번(직사각형 탈출)
if __name__ == '__main__':
    x, y, w, h = map(int, input().split())

    result = min(x, y, w - x, h - y)

    print(result)
