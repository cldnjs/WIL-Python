# 백준 온라인 1110번 문제
if __name__ == '__main__':
    data = int(input())

    temp = data
    count = 0

    while True:
        first_digit = temp // 10
        second_digit = temp % 10
        new_second_digit = (first_digit + second_digit) % 10
        temp = (10 * second_digit) + new_second_digit
        count += 1

        if temp is data:
            break

    print(count)
