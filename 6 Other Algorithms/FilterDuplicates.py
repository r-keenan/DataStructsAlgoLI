items = ["apple", "pear", "orange", "banana", "apple", "orange", "apple", "pear", "banana", "orange", "apple", "kiwi", "pear", "apple", "orange"]

# create a hash table to perform a filter
filter = dict()

# loop over each item and add to the hashtable
for key in items:
    filter[key] = 0

# create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)