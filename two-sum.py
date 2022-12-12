def two_sum(nums, target):
    """
    Given an array of integers, return the indices of the two numbers such that they add up to the target.
    Assume that each input would have exactly one solution, and you may not use the same element twice.
    
    :param nums: List[int]
    :param target: int
    :return: Tuple[int, int]
    """
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return seen[target - num], i
        seen[num] = i
    return None


"""
The runtime of the above solution is linear, or O(n), where n is the length of the input array (nums). This is because the solution uses a single loop to iterate over the input array, and the dictionary lookup and insertion operations have constant time complexity.

In more detail, the solution iterates over the input array once, and for each number it performs a constant-time lookup operation in the dictionary, and potentially inserts a new key-value pair into the dictionary. Since the dictionary has a fixed size (it can hold at most n key-value pairs, where n is the length of the input array), the time complexity of these operations does not depend on the input size, and is considered constant.

Therefore, the overall time complexity of the solution is O(n) (linear), which means it can handle large input sizes efficiently.
"""
