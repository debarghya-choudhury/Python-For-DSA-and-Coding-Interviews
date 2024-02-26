# while loop
print("\nwhile loop")

n = 0  # variable needs to be declared
while n < 5:
    print(n)
    n += 1


# for loop
print("\nfor loop")

print("\nex1")
for i in range(5):   # variable gets declared and set to 0 >>> i = 0
    print(i)    # i gets incremented gradually >>> 0 1 2 3 4

print("\nex2")
for i in range(2,6):
    print(i)

print("\nex3")
for i in range(5, 1, -1):  # decrement by 1 by using -1
    print(i)

# >>>
# ex3
# 5
# 4
# 3
# 2