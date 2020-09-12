def myAtoi(self, str: str) -> int:
    # strip the left side's whitespace
    s = str.lstrip()
    length = len(s)
    
    # edge case: empty string input
    if length == 0:
        return 0
    
    i = 0
    is_negative = False
    # take in sign, if there is one
    if s[0] == '+':
        i += 1
    elif s[0] == '-':
        is_negative = True
        i += 1
    
    digits = []
    # keep ingesting numbers
    while i < length and s[i].isnumeric():
        digits.append(int(s[i]))
        i += 1
    
    # if we couldn't find any digits, no conversion
    # should happen
    n_digits = len(digits)
    if n_digits == 0:
        return 0
    
    # turn digits into integer
    k = n_digits - 1
    result = 0
    power_of_ten = 0
    while k >= 0:
        result += ((10 ** power_of_ten) * digits[k])
        power_of_ten += 1
        k -= 1
        
    # check for overflow
    max_int = (2 ** 31) - 1
    print(max_int)
    min_int = -1 * (2 ** 31)
    print(min_int)
        
    result = -1 * result if is_negative else result
    
    if result > max_int:
        return max_int
    elif result < min_int:
        return min_int
    else:
        return result