import Gen
import List_and_tuples
import itertools
#update
t = False
times = 8
symbol = False
number = False

if __name__ == '__main__':
    # Generate password
    Gen.gen(times, t)

    print(List_and_tuples.Password)
    # Compare the password list to the other tuples
    for p, s, n in itertools.product(List_and_tuples.Password, List_and_tuples.Symbols, List_and_tuples.Numbers):
        # Check if there is at least 1 Symbol
        if p == s:
            symbol = True
        # Check if there is at least 1 Number
        if p == n:
            number = True
    print(f'\nSymbol: {symbol} Number: {number}')