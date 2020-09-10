def firstUniqChar(self, s: str) -> int:
    length = len(s)
    
    # keep track of elements you've already seen
    seen = list()
    
    # for every character you haven't seen yet,
    # return i if the rest of the list doesn't have
    # a duplicate
    for i in range(length):
        curr = s[i]
        duplicate_found = False
        if curr not in seen:
            seen.append(curr)
            k = i + 1
            while k < length:
                if s[k] == curr:
                    duplicate_found = True
                    break
                k += 1
            if not duplicate_found:
                return i
    
    return -1