def rotatelist(ll, shft):
    l = len(ll)
    shft = shft % l
    ans = ll[l-shft:] + ll[:l-shft]
    return ans

print rotatelist([1,2,3,4,5],1)
print rotatelist([1,2,3,4,5],3)
print rotatelist([1,2,3,4,5],12)