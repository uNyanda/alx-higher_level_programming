#!/usr/bin/python3
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs='*')
    args = parser.parse_args()

    num_args = len(args.args)
    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(args.args, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
