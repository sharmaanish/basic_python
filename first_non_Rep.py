def non_rep(ch):
    res = {}
    result = ''
    for c in ch:
        res[c] = res.get(c,0) + 1

    for c in res:
        if res[c] == 1:
            result=  c
    return result

print(non_rep('Swiss'))