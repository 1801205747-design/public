针对你的任务要求，这里为你梳理了八皇后问题的实现思路，以及标准的 Python 运行与测试流程。
1. 实现思路：回溯算法 (Backtracking)
八皇后问题的核心是在 8 \times 8 的棋盘上放置 8 个皇后，使其互不攻击（不在同一行、同一列或同一斜线上）。
 * 按行放置：我们逐行放置皇后，这样可以天然避免“行冲突”。
 * 冲突检查：在放置第 r 行的皇后到第 c 列时，检查前 r-1 行已放置的皇后：
   * 列冲突：是否有皇后已在第 c 列。
   * 对角线冲突：行差是否等于列差，即 |r_1 - r_2| = |c_1 - c_2|。
 * 递归与回溯：如果当前位置安全，则进入下一行；如果某一行所有位置都不安全，则退回上一行，尝试下一个位置。
2. 代码实现示例
src/queens.py (逻辑实现)
class QueensSolver:
    def solve(self, n):
        self.n = n
        self.solutions = 0
        self._backtrack(0, [])
        return self.solutions

    def _backtrack(self, row, columns):
        if row == self.n:
            self.solutions += 1
            return

        for col in range(self.n): # 故意引入 Bug 处：若改为 range(self.n - 1)
            if self._is_safe(row, col, columns):
                columns.append(col)
                self._backtrack(row + 1, columns)
                columns.pop() # 回溯

    def _is_safe(self, row, col, columns):
        for r, c in enumerate(columns):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

tests/test_queens.py (自动化测试)
import unittest
from src.queens import QueensSolver

class TestQueens(unittest.TestCase):
    def setUp(self):
        self.solver = QueensSolver()

    def test_n4(self):
        # N=4 时已知有 2 组解
        self.assertEqual(self.solver.solve(4), 2)

    def test_n8(self):
        # N=8 时已知有 92 组解
        self.assertEqual(self.solver.solve(8), 92)

3. 运行与测试方式
确保你在 hw01 根目录下执行以下命令：
A. 使用标准 unittest 运行
Python 自带的测试框架，无需安装额外包：
python -m unittest discover tests

B. 使用 pytest 运行 (推荐)
pytest 输出更清晰，如果未安装请先 pip install pytest：
# 在根目录直接运行，它会自动搜寻 tests 目录
pytest

C. 自主修复任务演示
 * 引入 Bug：将 queens.py 中的 range(self.n) 改为 range(self.n - 1)。
 * 触发报错：运行 pytest，你会看到测试失败（N=4 的解数会少于 2）。
 * AI 修复：你可以把报错信息贴给 AI，它会告诉你由于循环范围不足，导致最后一列永远无法放置皇后。
你需要我为你解释一下 _is_safe 函数中那个判断对角线的数学原理吗？
