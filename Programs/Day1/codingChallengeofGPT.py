a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b, a is b)
print( a == c, a is c)
c.append(4)
print(a)
print(b)
print(c)
