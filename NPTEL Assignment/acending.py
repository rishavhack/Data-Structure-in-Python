def ascending(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


print ascending([])
print ascending([3,3,4])
print ascending([7,18,17,19])