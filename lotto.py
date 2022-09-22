import random 

your_numbers = set()
lotto_numbers = set()


def game_choice():
    choice = input("\nIf you want to pick random numbers type 'draw', if not just press 'Enter': ")

    if choice == 'draw':
        get_random_numbers()
    elif choice == '':
        pass
    else:
        print('There is no choice like this!')
        game_choice()

    if len(your_numbers) < 6:
        input_numbers()
    
    return your_numbers

def input_numbers():
    for x in range(6):
        try:
            number = int(input('Input number that you choose: '))
            if number < 0 or number > 50:
                raise ValueError
        except ValueError:
            print('It is not correct number, please type integer in range(1,49)')
            continue

        your_numbers.add(number)

    while len(your_numbers) < 6:
        your_numbers.add(random.randint(1,49))

    return your_numbers


def get_random_numbers():
    while len(your_numbers) < 6:
        your_numbers.add(random.randint(1,49))
    return your_numbers


def get_lotto_numbers():
    lotto_numbers = set()
    while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1,49))
    return lotto_numbers


def check_win(your_numbers, lotto_numbers):
    return len(your_numbers.intersection(lotto_numbers))


def how_many_plays(your_numbers):   
    matches = 0 
    x = 0

    while matches < 6:
        x +=  1
        lotto_numbers = get_lotto_numbers()
        matches = check_win(your_numbers, lotto_numbers)
    
    return f'You will win after: {x} attempts,\
        \nYour numbers: {your_numbers},\
        \nLotto_numbers: {lotto_numbers},\
        \nYou will spend: {x*3}zl\
        \nYour win is 10000000zl\
        \nYou will win/lose {10000000-x*3}'


if __name__ == '__main__':
    game_choice()
    print(how_many_plays(your_numbers))
