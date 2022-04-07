from random import randint, choice
from re import search

operations = {1: "simple operations with numbers 2-9", 2: "integral squares of 11-29"}


class TypoError(Exception):
    def __str__(self):
        return "Incorrect format"


def check_typo(answer):
    """Check user input

    Raise error if input contains letters or it's empty.
    """
    if not answer or search("[A-z]", answer):
        raise TypoError
    else:
        return int(answer)


def check_level(lvl):
    if lvl not in [1, 2]:
        raise TypoError
    else:
        return lvl


def ask_level():
    global operations
    while True:
        print("Which level do you want? Enter a number:")
        for key, value in operations.items():
            print(value)

        try:
            level = check_level(int(input()))
        except TypoError as err:
            print(err)
        else:
            return level


def answer(result):
    """Check answer to an equations.

    Increases number of correct answer if user answer matches to
    the result
    """
    global counter
    global correct

    while True:
        try:
            usr_inp = check_typo(input())
        except TypoError as err:
            print(err)
        else:
            if result == usr_inp:
                correct += 1
                print("Right!")
            else:
                print("Wrong!")

            counter += 1
            break


def save_file(correct):
    """Save results in 'results.txt'

    Save results after positive answer.
    """
    inp_save = input(
        f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no."
    )
    if inp_save in ["yes", "YES", "y", "Yes"]:
        inp_username = input("What is your name?")
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{inp_username}: {correct}/5 in level {level} ({operations[level]})"
            )
            file.close()
        print('The results are saved in "results.txt".')


counter, correct = 0, 0
level = ask_level()

while counter < 5:
    if level == 1:
        # Generate easy task 3 + 4
        random_x, random_y = randint(2, 9), randint(2, 9)
        operator = choice(["+", "-", "*"])
        task = f"{random_x}{operator}{random_y}"
        print(task)

        result = eval(task)
        answer(result)

    elif level == 2:
        # Generate squre task 11 ** 2
        random_int = randint(11, 29)
        print(random_int)

        result = pow(random_int, 2)
        answer(result)

save_file(correct)
