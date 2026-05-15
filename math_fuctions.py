import math 
# Ceil
x = 4.5 #rounds up to 5
y = 4.2 #rounds up to 5
print(math.ceil(x))
print(math.ceil(y))

# Floor
a = 4.5 #rounds down to 4
b = 4.2 #rounds down to 4
c = -4.5 #rounds down to -5
d = 0.0076 #rounds down to 0
print(math.floor(a))
print(math.floor(b))
print(math.floor(c))
print(math.floor(d))

# Round
# .1 ---> rounds down to 0
# .5 ---> rounds up to 1
c = 4.5 #rounds to 4
d = 4.2 #rounds to 4
e = 809.455 #rounds to 809
f = 809.455 #rounds to 809.46
print(round(c))
print(round(d))
print(round(e))
print(round(f))