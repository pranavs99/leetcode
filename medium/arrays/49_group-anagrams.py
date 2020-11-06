def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # anagrams sort to the same string
    # map each sorted string to the indices of the anagrams' locations
    record = dict()
    for i in range(len(strs)):
        sorted_s = str(sorted(strs[i]))
        if record.get(sorted_s) is None:
            record[sorted_s] = [i]
        else:
            record[sorted_s].append(i)
            
    # iterate through the indices for each anagram
    # and group strs[i] for each group of indices
    result = []
    for key, value in record.items():
        result.append([strs[k] for k in value])
    
    return result