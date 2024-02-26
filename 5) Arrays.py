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
arr[0] = 12  # O(1)
