def ch_frq(ch):
    res = {}
    for i in ch:
        res[i] = res.get(i,0) + 1 
    
    return res

print(ch_frq('amazon'))