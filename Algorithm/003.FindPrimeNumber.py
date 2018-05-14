# 백준 온라인 1978번(소수 찾기)
def check_list(data, data_count):
    if len(data) != data_count:
        return False

    for item in data:
        if item > 1000:
            return False

    return True


def is_prime(number):
    if (number == 1) or number < 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    count = 0
    number_of_data = int(input())
    if number_of_data > 100:
        print('100이하를 입력해주세요')
        exit()

    number_list = list(map(int, input().split()))
    if not check_list(number_list, number_of_data):
        print('데이터의 개수가 맞지않거나 1000을 초과한 데이터가 있음')
        exit()

    for item in number_list:
        if is_prime(item):
            count += 1

    print(count)
