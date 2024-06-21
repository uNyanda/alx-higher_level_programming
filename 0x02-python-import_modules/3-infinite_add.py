#!/usr/bin/python3
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', type=int, nargs='*', default=[0])
    args = parser.parse_args()
    print(sum(args.numbers))


if __name__ == "__main__":
    main()
