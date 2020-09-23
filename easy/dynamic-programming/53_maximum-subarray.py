def maxSubArray(self, nums: List[int]) -> int:
    curr_sum = nums[0]
    result = nums[0]
    
    length = len(nums)
    if length <= 1:
        return result
    
    for i in range(1, length):
        curr_sum = max(nums[i], curr_sum + nums[i])
        result = max(result, curr_sum)
    
    return result