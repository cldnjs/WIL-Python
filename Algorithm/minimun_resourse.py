def get_min_resource(data_list):
    if len(data_list) == 1:
        return 0

    data_list.sort(reverse=True)
    min_sum = data_list.pop() + data_list.pop()
    data_list.append(min_sum)

    return min_sum + get_min_resource(data_list)


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    if not len(data) == n:
        exit()

    print(get_min_resource(data))
