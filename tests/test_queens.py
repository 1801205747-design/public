import unittest
import sys
from pathlib import Path

# Add src directory to path so we can import QueensSolver
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from queens import QueensSolver


class TestQueensSolver(unittest.TestCase):
    """Unit tests for QueensSolver class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solver = QueensSolver()
    
    def test_solve_n4_returns_2_solutions(self):
        """Test that N=4 has exactly 2 solutions."""
        result = self.solver.solve(4)
        self.assertEqual(result, 2, 
                        f"Expected 2 solutions for N=4, but got {result}")
    
    def test_solve_n8_returns_92_solutions(self):
        """Test that N=8 has exactly 92 solutions."""
        result = self.solver.solve(8)
        self.assertEqual(result, 92,
                        f"Expected 92 solutions for N=8, but got {result}")
    
    def test_solve_n0_returns_0(self):
        """Test that N=0 returns 0 solutions."""
        result = self.solver.solve(0)
        self.assertEqual(result, 0,
                        "Expected 0 solutions for N=0")
    
    def test_solve_n1_returns_1(self):
        """Test that N=1 has exactly 1 solution."""
        result = self.solver.solve(1)
        self.assertEqual(result, 1,
                        "Expected 1 solution for N=1")
    
    def test_solve_n2_returns_0(self):
        """Test that N=2 has no solutions."""
        result = self.solver.solve(2)
        self.assertEqual(result, 0,
                        "Expected 0 solutions for N=2")
    
    def test_solve_n3_returns_0(self):
        """Test that N=3 has no solutions."""
        result = self.solver.solve(3)
        self.assertEqual(result, 0,
                        "Expected 0 solutions for N=3")
    
    def test_solver_multiple_calls(self):
        """Test that solver can be called multiple times with different values."""
        result1 = self.solver.solve(4)
        result2 = self.solver.solve(8)
        result3 = self.solver.solve(4)
        
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 92)
        self.assertEqual(result3, 2,
                        "Solver should reset solutions_count on each solve() call")


if __name__ == '__main__':
    unittest.main()
