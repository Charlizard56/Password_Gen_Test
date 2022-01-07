import Gen
import List_and_tuples


t = False
times = 8
symbol = False
number = False
letters_lower = False
letters_upper = False

if __name__ == '__main__':

    while True:
        try:
            Gen.gen(times,t)
            print(List_and_tuples.Password_Gen)
            t = Gen.Check(symbol, number, letters_lower, letters_upper)
            if t:
                print("All True")
                # Crate String For Password
                List_and_tuples.Password = ""
                for p_g in List_and_tuples.Password_Gen:
                    List_and_tuples.Password += p_g
                    print(List_and_tuples.Password)
                break
            else:
                print("Continue")
                List_and_tuples.Password_Gen = []
                continue

        except:
            print("Something went wrong")

        finally:
            print("Password Generation Success!")




