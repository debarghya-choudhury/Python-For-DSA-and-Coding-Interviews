# Python has a syntax similar to the spread operator (...) in JavaScript, but it's called the "unpacking operator" or "splat operator." 
# In Python, the * operator is used for unpacking iterables like lists, tuples, dictionaries, and sets.

# Here's how we can use the unpacking operator in various contexts:

# Unpacking Iterables:
my_list = [1, 2, 3]
print(*my_list)  # Output: 1 2 3

# Concatenating Lists:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = [*list1, *list2]
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Unpacking Dictionaries:
my_dict = {'a': 1, 'b': 2}
print(*my_dict)  # Output: a b
print(**my_dict)  # Raises TypeError: '**' argument must be a mapping, not int

# Passing Arguments to Functions:
def my_function(a, b, c):
    print(a, b, c)

args = [1, 2, 3]
my_function(*args)  # Output: 1 2 3

# Unpacking Operator with Keyword Arguments:
def my_function2(a, b, c):
    print(a, b, c)

kwargs = {'a': 1, 'b': 2, 'c': 3}
my_function2(**kwargs)  # Output: 1 2 3

# The unpacking operator allows you to expand iterables into individual elements or key-value pairs, making it a powerful tool for working with collections and functions in Python.