def plusOne(self, digits: List[int]) -> List[int]:
    # force a +1 on the last digit
    digits[-1] += 1
    # correct the preceding digits by carrying 1s
    i = len(digits) - 1
    while i > 0:
        if digits[i] > 9:
            digits[i] = 0
            digits[i - 1] += 1
        i -= 1
    # edge case: if the first digit is now 10, change
    # it to 0 and append a 1 to the front of the list
    if digits[0] > 9:
        digits[0] = 0
        digits.insert(0, 1)
    return digits