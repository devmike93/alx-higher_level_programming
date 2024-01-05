#!/usr/bin/python3
import sys


class NQueenSolver:
    """
    N-Queens Solver Class:
    This class provides methods to solve the N-Queens problem.
    """
    def solve(self, n):
        """
        Solves the N-Queens problem for a given board size 'n'.

        Args:
            n (int): The size of the chessboard and the number of queens.

        Returns:
            list: A list of solutions,
                  where each solution is a list of queen positions.
        """
        solutions = []
        state = []
        self.search(state, solutions, n)
        return (solutions)

    def is_valid_state(self, state, n):
        """
        Checks if a state is valid for the N-Queens problem.

        Args:
            state (list): A list representing the current queen positions.
            n (int): The size of the chessboard and the number of queens.

        Returns:
            bool: True if the state is valid, False otherwise.
        """
        return (len(state) == n)

    def get_candidates(self, state, n):
        """
        Gets the valid candidates for the next queen placement in the state.

        Args:
            state (list): A list representing the current queen positions.
            n (int): The size of the chessboard and the number of queens.

        Returns:
            set: A set of valid candidate positions for the next queen.
        """
        if not state:
            return range(n)

        position = len(state)
        candidates = set(range(n))
        for row, col in enumerate(state):
            candidates.discard(col)
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return (candidates)

    def search(self, state, solutions, n):
        """
        Recursively searches for solutions to the N-Queens problem.

        Args:
            state (list): A list representing the current queen positions.
            solutions (list): A list to store the found solutions.
            n (int): The size of the chessboard and the number of queens.

        Returns:
            None
        """
        if self.is_valid_state(state, n):
            solutions.append(state.copy())
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()


def main():
    """Main function for solving the N-Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if number < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueenSolver()
    for solution in solver.solve(number):
        formated_list = [[i, solution[i]] for i in range(len(solution))]
        print(formated_list)


if __name__ == "__main__":
    main()
