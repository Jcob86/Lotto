from lotto import get_lotto_numbers, check_win

def test_draw_6_numbers():
    numbers = get_lotto_numbers()
    assert len(numbers) == 6
    print('Passed drawing')

def test_win():
    your_numbers = set(range(6))
    lotto_numbers = set(range(6))
    result = check_win(your_numbers, lotto_numbers)
    assert result == 6
    print('Passed win')

test_draw_6_numbers()
test_win()