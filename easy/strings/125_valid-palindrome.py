def isPalindrome(self, s: str) -> bool:
    # using a functional, "Pythonic" approach
    
    # filter out all characters for whom .isalnum() returned False
    alnum_only = list(filter(lambda x: x.isalnum(), [c for c in s]))        
    # lower case all letters
    lowercased = list(map(lambda x: x.lower() if x.isalpha() else x, alnum_only))  
    # check if it reads the same forwards and backwards
    return list(reversed(lowercased)) == lowercased