print("first program")

# Nothing in Python is hoisted, not variables, not functions, nothing****

# Variables are dynamicly typed

n = 0
print('n =', n)
# >>> n = 0

n = "abc"
print('n =', n)
# >>> n = abc

# Multiple assignments
n, m = 0, "abc"
# this means n = 0 and m = abc

print("m =", m, 'n =', n)

# template literal for python
print(f"m = {m}, n = {n}")  # Using f-strings:


# increment
n = n + 1 # good
n += 1    # good
# n++       # bad   Gives Syntax error


# None is null (absence of value)
n = 4
n = None
print("n =", n)
# >>> n = None
