import Gen
import List_and_tuples
import itertools
t = False
times = 3

if __name__ == '__main__':
    # Generate password
    Gen.gen(times, t)

    print(List_and_tuples.Password)
    for p, s in itertools.product(List_and_tuples.Password,List_and_tuples.Symbols):
        if p == s:
            print("True")