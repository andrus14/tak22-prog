import random

x = random.randint(0, 100)

guess = -1

while x != guess:

    guess = int(input('Paku arvu: '))

    if x > guess:
        print('Paku suurem')
    elif x < guess:
        print('Paku väiksem')
    elif x == guess:
        print('Õige!')