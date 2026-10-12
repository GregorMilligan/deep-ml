def add_two_numbers(l1, l2):
    # l1 and l2 are lists of digits in reverse order
    l1.reverse()
    l2.reverse()
    calc = int("".join(map(str, l1)))+int("".join(map(str, l2)))
    output = list(map(int, str(calc)))
    return output[::-1]