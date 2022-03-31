from random import randint, choice
random_x, random_y = randint(2, 9), randint(2, 9)
operator = choice(['+', '-', '*'])

print(random_x, operator, random_y)


if operator == '+':
    result = random_x + random_y
elif operator == '-':
    result = random_x - random_y
elif operator == '*':
    result = random_x * random_y


print('Right!' if result == int(input()) else 'Wrong!')