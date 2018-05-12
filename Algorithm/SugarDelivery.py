# 백준 온라인 2839번 문제(설탕 나르기)
def calculate_sugar(n):
    three_count = 0
    five_count = 0

    if (n > 5000) or (n < 3):
        print('범위는 3 ~ 5000사이입니다.')
        exit()

    while True:
        if n == 0:
            return five_count + three_count
        elif n < 0:
            return -1
        elif n % 5 == 0:
            n -= 5
            five_count += 1
        else:
            n -= 3
            three_count += 1


if __name__ == '__main__':
    n = int(input())
    print(calculate_sugar(n))
