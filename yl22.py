import random

choices = ['kivi', 'paber', 'käärid']

while True:

    print('0) ei soovi rohkem mängida')
    print('1) kivi')
    print('2) paber')
    print('3) käärid')
    user_choice = int(input('Tee valik '))

    if user_choice == 0:
        break

    computer_choice = random.randint(1, 3)

    print('Sinu valik oli', choices[user_choice-1])
    print('Arvuti valik oli', choices[computer_choice-1])

    if user_choice == computer_choice:
        print('Mäng jäi viiki')
    elif user_choice == 1 and computer_choice == 3 or user_choice == 2 and computer_choice == 1 or user_choice == 3 and computer_choice == 2:
        print('Sinu võit')
    else:
        print('Arvuti võit')
    
    print()