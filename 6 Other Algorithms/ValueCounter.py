items = ["apple", "pear", "orange", "banana", "apple", "orange", "apple", "pear", "banana", "orange", "apple", "kiwi", "pear", "apple", "orange"]

# create hash table object ot hold the items and counts
counter = dict()

# iterate over each item and increment the count for each one
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

# print the results
print(counter)