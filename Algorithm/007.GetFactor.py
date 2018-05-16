# 백준 온라인 1037번(약수)
if __name__ == '__main__':
    n = int(input())
    factor_list = list(map(int, input().split()))

    print(min(factor_list) * max(factor_list))  # 가장 작은 약수와 가장 큰 약수의 곱
