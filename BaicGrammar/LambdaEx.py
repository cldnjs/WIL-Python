def func(a, b):
    return a + b


if __name__ == '__main__':
    result_def = func(1, 2)

    f = lambda x, y: x + y
    result_lambda = f(1, 2)

    print(result_def)
    print(result_lambda)
