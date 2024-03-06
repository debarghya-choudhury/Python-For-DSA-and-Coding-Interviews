# sort() modifies riginal list. 
# sorted() returns a new sorted list without modifying the original list.

    # Using sort():

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nums.sort()
print(nums)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    # Using sorted():

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_nums = sorted(nums)
print(sorted_nums)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(nums)         # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
