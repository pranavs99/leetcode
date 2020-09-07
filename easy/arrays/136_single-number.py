def singleNumber(self, nums: List[int]) -> int:
    nums = sorted(nums)
    length = len(nums)        
    if length > 1:
        if nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        # iterate through the elements and look any element
        # surrounded by two distinct elements
        for i in range(1, length - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
    else:
        return nums[0]