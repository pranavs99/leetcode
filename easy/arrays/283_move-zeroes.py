def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n_zeroes = nums.count(0)
    for i in range(n_zeroes):
        nums.remove(0)
        nums.append(0)
    return nums