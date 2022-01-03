items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def isSorted(itemlist):
    # brute force method
    #for i in range(0, len(itemlist) - 1):
    #    if (itemlist[i] > itemlist[i+1]):
    #        return False

    # all returns a boolean result. this uses list iteration
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    #return True

print(isSorted(items1))
print(isSorted(items2))