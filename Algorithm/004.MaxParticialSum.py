import sys

# 백준 온라인 192번 문제(연속합)
def check_list(data, size):
    if len(data) != size:
        return False

    for item in data:
        if (item < -1000) or (item > 1000):
            return False

    return True


def max_sub_array(a, size):
    max_so_far = -sys.maxsize
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


if __name__ == '__main__':
    n = int(input())
    if (n > 100000) or (n < 0):
        exit()

    data_list = list(map(int, input().split()))
    if not check_list(data_list, n):
        exit()

    print(max_sub_array(data_list, n))
