if __name__ == '__main__':
    # list Comprehension
    areas2 = [i * i for i in range(1, 11) if i % 2 == 0]
    print(areas2)

    list_a = [(x, y) for x in range(3) for y in range(3)]
    print(list_a, '\n')

    # Dictionary comprehension
    students = ['몽키', '선샤인', '시와', '톰']
    for number, name in enumerate(students):
        print('{}번의 이름은 {}입니다'.format(number + 1, name))

    students_dic = {
        '{}번'.format(number + 1): name for number, name in enumerate(students)
    }
    print(students_dic, '\n')

    # zip()함수를 이용한 Dictionary 생성
    students = ['몽키', '선샤인', '시와', '톰']
    scores = [85, 92, 78, 100]

    score_dic = {
        students: score for students, score in zip(students, scores)
    }
    print(score_dic)
