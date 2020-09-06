def removeDuplicates(self, nums: List[int]) -> int:
    # keep track of length because every removed duplicate
    # decreases the length of "nums"
    length = len(nums)

    # iterate through "nums"
    i = 0
    while i < length:
        curr_num = nums[i]

        # iterate through following elements as long as they're
        # duplicates and not "falling off the edge" of the array
        next = i + 1
        while next < length and nums[next] == curr_num:
            nums.remove(curr_num)
            # decrement length
            length -= 1

        # increment index "i" by only 1 because all the duplicates
        # between curr_num and the next distinct number have
        # been removed
        i += 1

    # since we've been keeping track of removals, the final length
    # should reflect the length of the modified list
    return length