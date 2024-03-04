# In Python, del and clear() serve different purposes when working with dictionaries.

#     del is used to delete specific elements (keys and their associated values) or even entire variables.
#     clear() is used to remove all elements from the dictionary, leaving it empty.

# Here's a breakdown of their usage:

a = {
    "name": "meow",
    "type": "cat"
}

# Remove a specific key-value pair
del a["type"]

# After executing this code, the dictionary a will become {"name": "meow"}.

# You can also use del to delete the entire dictionary:
a = {
    "name": "meow",
    "type": "cat"
}

# Delete the entire dictionary
del a


# clear():
# Remove all key-value pairs from the dictionary
a = {
    "name": "meow",
    "type": "cat"
}

a.clear() # >>> a = {}


# remove() for arrays
arr = [1,2,3]
arr2 = [1,2,3]

# both work
arr.remove(1)  
del arr2[0]    # del works for both dictionaries and arrays (lists)

print(arr, arr2)   # >>  [2, 3]  [2,3]