def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    
    lengths = [len(s) for s in strs]
    min_length = min(lengths)
    result = ""
    
    for i in range(min_length):
        curr_letter = strs[0][i]
        anyMismatches = False
        
        for j in range(1, len(strs)):
            if strs[j][i] != curr_letter:
                anyMismatches = True
                break
                
        if anyMismatches:
            return result
        else:
            result += curr_letter
            
    return result