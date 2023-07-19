from dataclasses import dataclass


@dataclass
class Solution:
    array: list
    k: int
    
    def find_largest(self):
        # O(n) time, O(1) space
        max_value = None
        for i in range(len(self.array)):
            if max_value is None or self.array[i] > max_value:
                max_value = self.array[i]
        
            return max_value

    def find_sorted(self):
        # O(nlogn) time, O(1) space
        self.array.sort()
        return self.array[-self.k]

    def find_repeated(self):
        # O(k) time
        for i in range(self.k - 1):
            # O(n) + O(n) time, O(1) space
            self.array.remove(max(self.array))
        
        # O(kn) time, O(1) space
        return self.array[-1]

    def find_heap(self):
        # O(n + klogn) time, O(n) space
        pass



args_and_expected = (
    ([1, 6, 43, 7, 3, 7, 10, 4, 8, 2], 3, 8),
    ([1, 6, 43, 7, 3, 7, 10, 4, 8, 2], 4, 7)
)

for (array, k, expected) in args_and_expected:
    sorted_solution = Solution(array, k).find_sorted()
    assert sorted_solution == expected, f"{sorted_solution} vs {expected}"
    
    repeated_solution = Solution(array, k).find_repeated()
    assert repeated_solution == expected, f"{repeated_solution} vs {expected}"
