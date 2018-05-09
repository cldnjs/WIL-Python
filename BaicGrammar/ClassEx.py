class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Person obj Created')

    def self_introduce(self):
        print('My name is {0} and I am {1} years old'.format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        print('Student obj Created')

    def self_introduce(self):
        print('I name is {0} and I am {1} years old and I am {2} grade'.format(self.name, self.age, self.grade))


if __name__ == '__main__':
    p = Person('chiwon', 19)
    s = Student('chiwon', 19, 3)

    if issubclass(type(s), type(p)) is True:
        print('right')
    else:
        print('not')
