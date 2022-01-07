import Gen
import List_and_tuples
import itertools

t = False
times = 8
symbol = False
number = False
letters_lower = False
letters_upper = False

if __name__ == '__main__':
    # Generate password
    Gen.gen(times, t)

    print(List_and_tuples.Password)
    # Compare the password list to the other tuples
    for p, s, n, l, L in itertools.product(List_and_tuples.Password, List_and_tuples.Symbols, List_and_tuples.Numbers,
                                        List_and_tuples.letters, List_and_tuples.Letters):
        # Check if there is at least 1 Symbol
        if p == s:
            symbol = True
        # Check if there is at least 1 Number
        if p == n:
            number = True
        if p == l:
            letters_lower = True
        if p == L:
            letters_upper = True



    print(f'\nSymbol: {symbol} | Number: {number} | Lowercase: {letters_lower}| Upper: {letters_upper}')