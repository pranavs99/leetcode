def rob(self, nums: List[int]) -> int:
    n_houses = len(nums)
    if n_houses < 1:
        return 0
    result = [0, nums[0]]
    n_houses = len(nums)
    for i in range(1, n_houses):
        rob_current_house = nums[i] + result[0]
        skip_current_house = result[1]            
        current = max(rob_current_house, skip_current_house)
        result[0] = result[1]
        result[1] = current
    return result[1]