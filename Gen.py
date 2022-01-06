import  random as r
import List_and_tuples


def ran():
    n = r.randint(0, len(List_and_tuples.List) - 1)
    for key,v in List_and_tuples.List.items():
            if(n == key):
                return v

def gen(times, t):
    _times = times
    _t = t
    # So the string array isn't empty
    List_and_tuples.Password.append(ran())
    print(f"Starting: {List_and_tuples.Password[0]}")

    while _times > 0:
        n = ran()
        l = List_and_tuples.Password[len(List_and_tuples.Password) - 1]

        print(f"Random: {n} Last: {l}")

        #Turn Upper or Lower Letters
        upper = r.randint(0,1)
        print(upper)
        if upper:
            try:
                n = n.upper()
            except:
                n = n

        # Check if letter,num or char was used last
        if n != l:
            List_and_tuples.Password.append(n)
            _times -= 1




