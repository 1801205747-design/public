class QueensSolver:
    """A class to solve the N-Queens problem."""
    
    def __init__(self):
        self.solutions_count = 0
    
    def solve(self, n):
        """
        Solve the N-Queens problem and return the number of all possible solutions.
        
        Args:
            n (int): The number of queens (and board size n x n)
            
        Returns:
            int: The total number of valid solutions
        """
        self.solutions_count = 0
        if n <= 0:
            return 0
        
        # Initialize the board state and columns/diagonals tracking
        board = [-1] * n  # board[i] = j means queen at row i, column j
        cols = set()      # columns occupied
        diag1 = set()     # diagonals (row - col)
        diag2 = set()     # diagonals (row + col)
        
        self._backtrack(0, n, board, cols, diag1, diag2)
        return self.solutions_count
    
    def _backtrack(self, row, n, board, cols, diag1, diag2):
        """
        Recursively place queens using backtracking.
        
        Args:
            row (int): Current row being processed
            n (int): Board size
            board (list): Current board state
            cols (set): Set of occupied columns
            diag1 (set): Set of occupied diagonals (row - col)
            diag2 (set): Set of occupied diagonals (row + col)
        """
        # Base case: all queens are placed
        if row == n:
            self.solutions_count += 1
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            # Check if this position is safe
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            # Place the queen
            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            # Recursively place the next queen
            self._backtrack(row + 1, n, board, cols, diag1, diag2)
            
            # Remove the queen (backtrack)
            board[row] = -1
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)