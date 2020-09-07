def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = list()
    # iterate through elements in nums1
    for n1 in nums1:
        # iterate through nums2, looking for a match
        for n2 in nums2:
            # if a match is found, append it to the result
            # and remove it from nums2 for efficiency
            if n1 == n2:
                result.append(n1)
                nums2.remove(n2)
                break
    return result