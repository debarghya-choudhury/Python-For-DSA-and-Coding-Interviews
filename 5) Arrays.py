# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)


# Can be used as a stack
arr.append(4)    # push basically   O(1)
arr.append(5)
print(arr)

arr.pop()   # O(1)
print(arr)

arr.insert(1, 7)  # O(n)  inserting 7 at arr[1], then adjusting list  
print(arr)

# read value
print(arr[0])

# reassign value
arr[0] = 12  # O(1) constant time operation

# Initialize arr of size n with default value of 1
n = 5 # length of arr
arr = [0] * n
print(arr)
print("length of array =", len(arr))

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is the second to last value, etc.
print(arr[-2])

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
arr2 = arr[1:3]
print(arr2)

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

# But no out of bounds error
print(arr[0:10])

# Unpacking Operator *      similar to spread operator ... in js 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = [*list1, *list2]
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Another ways for concatinating list
list3 = [1, 2, 3]
list4 = [4, 5, 6]
concatenated_list2 = list3 + list4   # ********
self_concatinated_list = list3 * 2   # ********