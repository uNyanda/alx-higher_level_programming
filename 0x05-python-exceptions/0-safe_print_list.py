#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for num in my_list:
        if counter >= x:
            break
        try:
            print(num, end="")
            counter += 1
        except Exception:
            pass
    print()
    return counter
