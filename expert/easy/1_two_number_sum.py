from enum import Enum
from typing import Any, Callable, List


class TwoNumberSumStrategy(Enum):
    NESTED_LOOP = "nested_loop"
    HASH = "hash"


class TwoNumberSum:
    def __init__(self, array: List[int], target: int):
        self.array = array
        self.target = target
    
    def solve(self, strategy: TwoNumberSumStrategy = TwoNumberSumStrategy.NESTED_LOOP) -> List[int]:
        method: Callable = self._get_method(strategy)
        return method()

    def _get_method(self, strategy: TwoNumberSumStrategy) -> Any:
        method_map = {
            TwoNumberSumStrategy.NESTED_LOOP: self._solve_nested_loop,
            TwoNumberSumStrategy.HASH: self._solve_hash
        }
    
        return method_map[strategy]

    def _solve_hash(self) -> List[int]:
        # O(n) time, O(n) space
        hashed = {
            self.array[i]: i
            for i in range(len(self.array))
        }
        
        for i in range(len(self.array)):
            complement = self.target - self.array[i]
            if complement in hashed and complement != self.array[i]:
                return [i, hashed[complement]]
        
        return [-1, -1]

    def _solve_nested_loop(self) -> List[int]:
        # O(n^2) time, O(1) space
        for i in range(len(self.array)):
            for j in range(i + 1, len(self.array)):
                if self.array[i] + self.array[j] == self.target:
                    return [i, j]
        
        return [-1, -1]

ex1 = [3, 5, -4, 8, 11, 1, -1, 6]
assert TwoNumberSum(ex1, 10).solve(strategy=TwoNumberSumStrategy.HASH) == [4, 6]
assert TwoNumberSum(ex1, 10).solve(strategy=TwoNumberSumStrategy.NESTED_LOOP) == [4, 6]

ex1 = [3, 5, -4, 8, 11, 1, 6]
assert TwoNumberSum(ex1, 10).solve(strategy=TwoNumberSumStrategy.HASH) == [-1, -1]
assert TwoNumberSum(ex1, 10).solve(strategy=TwoNumberSumStrategy.NESTED_LOOP) == [-1, -1]

ex1 = [3, 5, -4, 8, 11, 1, 6, 12, 9, 34, 23, 15]
assert TwoNumberSum(ex1, 40).solve(strategy=TwoNumberSumStrategy.HASH) == [6, 9]
assert TwoNumberSum(ex1, 40).solve(strategy=TwoNumberSumStrategy.NESTED_LOOP) == [6, 9]