def first_and_last_index(array, target: int):
    indices = []
    for i in range(len(array)):
        if array[i] == target and (i == 0 or array[i-1] < target):
            indices.append(i)
        if array[i] == target and (i == len(array) - 1 or array[i+1] > target):
            indices.append(i)
    
    if len(indices) != 0:
        return indices
    
    return [-1, -1]    


def first_and_last_index_binary(array, target: int):
    def _binary(array, target: int, first_index: int, last_index: int, find_first: bool = True, rec: int = 0):
            
        if first_index > last_index:
            return -1
        
        middle = (first_index + last_index) // 2
        
        if array[middle] == target:  
            if find_first:
                if middle == 0 or array[middle - 1] < target:
                    return middle
                else:
                    return _binary(array, target, first_index, middle - 1, find_first, rec+1)
            else: # find last
                if middle == len(array) - 1 or array[middle + 1] > target:
                    return middle
                else:
                    return _binary(array, target, middle + 1, last_index, find_first, rec+1)
        
        if array[middle] > target:
            return _binary(array, target, first_index, middle - 1, find_first, rec+1)
        
        if array[middle] < target:
            return _binary(array, target, middle + 1, last_index, find_first, rec+1)
    
    first = _binary(array, target, 0, len(array) - 1)
    last = _binary(array, target, 0, len(array) - 1, find_first=False)

    return [first, last]
    
expected_args_with_results = [
    ([1, 4, 6, 8, 8, 8, 9, 10, 12], 8, [3, 5]),
    ([1, 4, 6, 8, 10, 12], 8, [3, 3]),
    ([1, 4, 6, 10, 12], 8, [-1, -1]),
    ([1, 4, 6, 8, 8], 8, [3, 4]),
    ([8, 8, 9], 8, [0, 1]),
    ([8, 8], 8, [0, 1])
]

for _callable in (first_and_last_index_binary, first_and_last_index_binary):
    for i, (array, target, expected) in enumerate(expected_args_with_results):
        assert _callable(array, target) == expected, f"{_callable} failed: {_callable(array, target)} for {array}, {target} differs from {expected}"