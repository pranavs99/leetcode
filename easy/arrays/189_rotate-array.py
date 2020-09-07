def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # define an inline helper function that reverses
    # only the elements from indices i to j, inclusive
    def reverse(i, j):
        if j == i or i > j:
            return
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        reverse(i + 1, j - 1)
    
    length = len(nums)
    
    # a rotation by any multiple of length + k is the same
    # as a rotation by k
    if k >= length:
        k = k % length
    # edge case:
    # if the array doesn't need to be rotated, don't bother
    # any further
    if k == 0:
        return
    
    # reverse the entire array        
    reverse(0, len(nums) - 1)
    # reverse the first k elements
    reverse(0, k - 1)
    # reverse the last k elements
    reverse(k, length - 1)