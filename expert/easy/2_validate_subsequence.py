from enum import Enum
from typing import List

# subsequence: 

class ValidationStrategy(Enum):
    NESTED_LOOP = "nested_loop"
    HASH = "hash"
    BEST = "best"


class SubsequenceValidator:
    def __init__(self, sequence: List[int], subsequence: List[int]):
        self.sequence = sequence # len = n
        self.subsequence = subsequence # len = m
    
    def validate(self, strategy: ValidationStrategy = ValidationStrategy.NESTED_LOOP) -> bool:
        method = self._get_method(strategy)
        return method()

    def _get_method(self, strategy: ValidationStrategy):
        method_map = {
            ValidationStrategy.NESTED_LOOP: self._validate_nested_loop,
            ValidationStrategy.HASH: self._validate_hash,
            ValidationStrategy.BEST: self._validate_best
        }

        return method_map[strategy]

    def _validate_nested_loop(self) -> bool:
        """O(n*m) T, O(1) S"""
        start_index = 0
        # O(m)
        for sub_item in self.subsequence:
            # O(n)
            try:
                item_index = self.sequence[start_index:].index(sub_item)
            except:
                return False
            start_index = start_index + item_index + 1
        
        return True


    def _validate_hash(self) -> bool:
        """O(n+m) T, O(n2) S"""
        index_to_posterior_items_map: dict[int, set] = {}
        # O(n) T, O(n2) S
        for i, item in enumerate(self.sequence):
            index_to_posterior_items_map[item] = set(self.sequence[i:])
        
        # O(m) T, O(1) S
        for i, item in enumerate(self.subsequence):
            posterior_items = index_to_posterior_items_map.get(item, None)
            item_not_in_sequence = posterior_items is None
            next_item_not_in_posterior_items = (
                self.subsequence[i+1] not in posterior_items
                if i < len(self.subsequence) - 1
                else False
            )
            if item_not_in_sequence or next_item_not_in_posterior_items:
                return False
        
        return True

    def _validate_best(self):
        """O(n) T, O(1) S"""
        sub_index = 0
        for item in self.sequence:
            if sub_index == len(self.subsequence):
                return True
            if item == self.subsequence[sub_index]:
                sub_index += 1
        
        return sub_index == len(self.subsequence)


args_and_expected = (
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
    ([2,7,4,9,5, 12, 17, 15, 19, 20, 65, 78], [2, 12, 65], True),
    ([2,7,4,9,5, 12, 17, 15, 19, 20, 65, 78], [2, 12, 78], True),
    ([2,7,4,9,5, 12, 17, 15, 19, 20, 65, 78], [2, 12, -68], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -5, 10], False),
)

for (sequence, subsequence, expected) in args_and_expected:
    for strategy in ValidationStrategy:
        actual = SubsequenceValidator(sequence, subsequence).validate(strategy)
        if actual != expected:
            print("\nWRONG\n")
        else:
            print("COOL")
        print(f"{strategy.value} - {sequence} vs {subsequence} - {expected} vs {actual}")