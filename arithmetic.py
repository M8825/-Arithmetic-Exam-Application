from random import randint, choice
from re import search


class TypoError(Exception):
    def __str__(self):
        return 'Incorrect format'


def check_typo(answer):
    if not answer or search('[A-z]', answer):
        raise TypoError
    else:
        return int(answer)


counter, correct = 0, 0
while counter < 5:
    random_x, random_y = randint(2, 9), randint(2, 9)
    operator = choice(['+', '-', '*'])
    task = f"{random_x}{operator}{random_y}"
    print(task)

    result = eval(task)
    while True:
        try:
            usr_inp = check_typo(input())
        except TypoError as err:
            print(err)
        else:
            if result == usr_inp:
                correct += 1
                print('Right!')
            else:
                print('Wrong!')

            counter += 1
            break

print(f'Your mark is {correct}/5')
