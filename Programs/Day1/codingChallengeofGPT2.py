# 1. Small integers (-5 to 256 are cached in Python)
x = 256
y = 256
print("Small ints:", x == y, x is y)

# 2. Large integers (not cached by default)
x = 257
y = 257
print("Large ints:", x == y, x is y)

# 3. Strings - short literals are interned
s1 = "hello"
s2 = "hello"
print("Short strings:", s1 == s2, s1 is s2)

# 4. Strings - created differently (might break interning)
s3 = "".join(["he", "llo"])
print("Joined string vs literal:", s1 == s3, s1 is s3)

# 5. Tuples - immutable but still can be different objects
t1 = (1, 2)
t2 = (1, 2)
print("Small tuples:", t1 == t2, t1 is t2)

# 6. Lists - always new objects unless explicitly assigned
l1 = [1, 2]
l2 = [1, 2]
print("Lists:", l1 == l2, l1 is l2)

