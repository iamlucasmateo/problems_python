from typing import List

# Takeaway to solve it in O(N): break the array in two parts, keeping track of the two indices with a while loop.

class SquaredSortedArray:
    """Given a sorted array of (possibly negative) ints, returned the sorted array of itsd squares."""
    def __init__(self, array: List[int]):
        self.array = array
    

    def solve(self):
        first_positive_index = None
        # O(N) T, O(1) S
        for i, item in enumerate(self.array):
            if item >= 0:
                first_positive_index = i
                break

        all_ints_have_the_same_sign: int = first_positive_index in [0, None]
        # O(N) TS
        if all_ints_have_the_same_sign:
            return [x*x for x in self.array]

        negative_index, positive_index = 0, first_positive_index
        negatives_remaining, positives_remaining = True, True
        squared = [] 
        # O(N) T, O(N) S
        while True:            
            negatives_remaining = negative_index < first_positive_index
            positives_remaining = positive_index < len(self.array)
            if not (negatives_remaining or positives_remaining):
                break
            elif negatives_remaining and positives_remaining:
                negative_abs_value = -self.array[negative_index]
                positive_value = self.array[positive_index]
                if negative_abs_value < positive_value:
                    squared.append(negative_abs_value**2)
                    negative_index += 1
                else: 
                    squared.append(positive_value**2)
                    positive_index += 1
            elif negatives_remaining:
                negative_abs_value = -self.array[negative_index]
                squared.append(negative_abs_value**2)
                negative_index += 1
            else:
                positive_value = self.array[positive_index]
                squared.append(positive_value**2)
                positive_index += 1
        
        return squared


args_and_expected = (
    ([1, 2, 3], [1, 4, 9]),
    ([-1, -2, -3], [1, 4, 9]),
    ([-1, -2, -3, 1, 2, 3], [1, 1, 4, 4, 9, 9]),
    ([-1, -4, -7, -9, 2, 3, 5, 8], [1, 4, 9, 16, 25, 49, 64, 81]),
)

for arr, expected in args_and_expected:
    solution = SquaredSortedArray(arr).solve()
    if solution == expected:
        print("COOL")
    else:
        print("WRONG")
    print(arr, solution, expected)