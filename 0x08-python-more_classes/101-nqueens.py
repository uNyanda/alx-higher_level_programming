#!/usr/bin/python3

"""
This module provides a solution for the N-Queens
problem using a backtracking algorithm.

The N-Queens problem is a classic computer science problem.
The goal is to place N queens on an NxN chessboard such that
no two queens threaten each other. This solution uses a backtracking
algorithm to place queens one by one in different columns, starting
from thhe leftmost column. When placing a queen in a column, it
checks for clashes with already placed queens. If a queen can be
placed in current column, the functioin recurs for the next
column. If no place can be found for the current queen in the
current column, it returns false and the queen in the previous
column is removed (backtracked). If all queens are placed, it
prints the solution.

Functions:
- solve_n_queens(n, i=0, a=[]): Solves the N-Queens problem using backtracking.
- is_valid(a): Checks if the current arrangement of queens is valid.
- main(): The main entry point of the program. It validates the command line
    arguments and calls the solve_n_queens function.

If the script is run as the main module, the main function is called.
If the script is imported as a module, the main function is not called.
The solve_n_queens and is_valid functions can be used independently in
other programs to solve the N-Queens problem.
"""
import sys

def solve_n_queens(n, i=0, a=[]):
    """
    This function solves the N-Queens problem
    using backtracking.

    Parameters:
    n (int): The number of queens
        (and the size of the chessboard).
    i (int): The current row index.
        Default is 0.
    a (list): The current arrangement of queens.
        Default is an empty list.
    """
    if i == n:  # if all queens are placed.
        print(a)  # print the arrangement of queens.
        return

    for j in range(n):  # for every column in the current row
        a.append(j)  # place the queen in the current column
        if is_valid(a):  # if the current arrangement of queens is valid.
            solve_n_queens(n, i + 1, a)  # recur for the next row
        a.pop()  # if placing isn't the solution, the remove the queen (backtrack)

    def is_valid(a):
        """
        This function checks if the current arrangement of queens
        is valid.
        """
        i = len(a) - 1  # get the index of the latest queen placed
        for j in range(i):  # for every queen placed so far
            if a[i] == a[j] or a[i] - i == a[j] - j or a[i] + i == a[j] + j:
                # if the last queen placed is in the same column or
                # on the same diagonal as any of the previous queens
                return False  # the arrangement is not valid
        return True  # if no conflicts with any of the queens,
        # the arrangement is a valid.

    def main():
        """
        This function is the main entry point of the program.
        It validates the command line arguments and calls the
        solve_n_queens function.
        """
        if len(sys.argv) != 2:  # if the number of command line arguments != 2.
            print("Usage: nqueens N")
            sys.exit(1)  # print usage message and exit.

        try:  # try to convert the second command line to an integer.
            n = int(sys.argv[1])
        except ValueError:  # print error message if not integer.
            print("N must be a number")
            sys.exit(1)

        if n < 4:  # if the number of queens is less than 4.
            print("N must be at least 4")  # print err. message and exit.
            sys.exit(1)
        solve_n_queens(n)  # call the solve_n_queens function with no. queens

    if __name__ == "__main__":  # if the script is run as the main module.
        main()  # call the main function
