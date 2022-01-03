items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def findMax(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]
    # else get the first item and call the function
    # again to operate on teh rest of the list
    op1 = items[0]
    op2 = findMax(items[1:])

    # perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2

# test the function
print(findMax(items))