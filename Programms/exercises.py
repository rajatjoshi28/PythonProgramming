# 1) Basic assignments
# TODO: create variables name (str), age (int), height_m (float), is_employed (bool)

name = "Rajat"
age = 26
height_m = 5.7
is_employed = True

print([1], name, "Who is", age, "Old and height is", height_m, "is currently employed", is_employed)
# 2) Arithmetic & precedence
# Compute simple expression and show precedence using parentheses
# TODO: set result to 2 + 3 * 4 ** 2  and result2 to the same expression but fully parenthesized
result1 =26
result2 = 2 + (3*(4*2))
print("[2]", result1, result2)

# 3) Type conversion
# TODO: Convert "42" to int and "3.14" to float and sum them
x=int("42")
y=float("3.14")
print("[3]", "total :", x+y)

# 4) Division vs floor division
# TODO: compute 5/2 and 5//2
a=5/2
b=5//2
print("[4]", a, b)

# 5) f-strings vs concatenation
# TODO: create a greeting using f-string and using concatenation
a = "hello"
b = "Rajat"
print("[5] "f"{a} {b}", a, b)

# 6) Truthiness
# TODO: fill truthy and falsy values examples
truthy_values = [True, 12,"123"]
falsy_values = [0,{}]
print("[6] truthy:", [bool(v) for v in truthy_values], "falsy:", [bool(v) for v in falsy_values])


# 7) Identity vs equality
x1 = [1, 2, 3]
x2 = [1, 2, 3]
# TODO: eq should be True, ident should be False
eq = (x1 == x2)
ident = (x1 is x2)
print("[7] ==", eq, "| is", ident)

# 8) Unpacking & swapping
# TODO: swap variables using tuple unpacking
a=10
b=20
print("[8]", b,a)

# 9) Rounding
# TODO: round 3.14159 to 2 decimal places
pi = 3.14159
pi2 = round(pi,2)
pi2f = f"{pi :.2f}"
print("[9]", pi2, pi2f)


# 10) Safe int parsing
# TODO: write a function safe_int(s) that returns int(s) or None if cannot parse
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None

print("[10]", safe_int("123"), safe_int("12.3"), safe_int("abc"))



# 11) Small calculator
# TODO: write a function calc(a, b) that returns dict with sum, diff, prod, quot (float)
def calc(a, b):
    return {
        "sum": a + b,
        "diff": a - b,
        "prod": a * b,
        "quot": float(a) / b
    }

print("[11]", calc(7, 3))


# 12) List/Dict basics
# TODO: Given list of scores, compute average and build dict with min/max/avg
scores = [88, 92, 76, 90, 85]
sum = sum(scores)
count = len(scores)
avg = sum/count
summary = {"min": min(scores), "max": max(scores), "avg": avg}
print("[12]", summary)

