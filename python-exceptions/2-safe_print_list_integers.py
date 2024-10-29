#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break
    print()
    return count

if __name__ == "__main__":
    my_list = [1, 2, 'a', 3, 4, 'b', 5]
    nb_print = safe_print_list_integers(my_list, 5)
    print(f"nb_print: {nb_print}")
    nb_print = safe_print_list_integers(my_list, 7)
    print(f"nb_print: {nb_print}")
