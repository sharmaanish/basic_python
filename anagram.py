def anagram(ch1, ch2):
    if len(ch1) != len(ch2):
        return False
    counts_res = {}

    for c in ch1:
        counts_res[c] = counts_res.get(c,0) + 1 
    
    for c in ch2:
        if c not in counts_res:
            return False
        counts_res[c] -= 1

        if counts_res[c] <0:
            return False

    return True 

print(anagram('aaa', 'aab'))