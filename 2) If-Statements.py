# If statements don't need parentheses 
# or curly braces.

n = 1
if n % 3 == 0 and n % 5 == 0:
    print("fizzbuzz")
elif n % 3 == 0:
    print("buzz")
elif n % 5 == 0:
    print("fizz")
else:
    print("invalid")    


# Parentheses needed for multi-line conditions.
# and = &&
# or  = ||
    
n, m = 1, 2    # example
if ((n > 2 and 
    n != m) or n == m):
    n += 1