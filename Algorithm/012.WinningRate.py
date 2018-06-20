import math


def plus_one_percent(total_game, won_game):
    rate = won_game / total_game * 100

    goal_rate = rate + 1
    x = (goal_rate * total_game - 100 * won_game) / (100 - goal_rate)

    return math.ceil(x)


if __name__ == '__main__':
    total = int(input('게임 횟수: '))
    win_game = int(input('이긴 횟수: '))

    win_rate = win_game / total * 100

    if win_rate >= 99:
        print('승률이 100%이상일 수는 없습니다.')
        exit(-1)

    print('승률은 {0}%입니다.'.format(win_rate))

    print('승률이 {0}%가 되려면 최소 {1}게임을 해야합니다.'
          .format(win_rate + 1, plus_one_percent(total, win_game)))
