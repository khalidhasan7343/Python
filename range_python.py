a =list(range(10))
b = tuple(range(10))
c = list(range(1, 10 , 2))
# range(start, stop, step)
d = list(range(1, 100 , 5))
e = list(range(10, 0 , -1))
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(c) # [1, 3, 5, 7, 9]
print(d) # [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
print(e) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
