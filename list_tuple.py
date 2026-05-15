a = [1, 2, 3, "rahat", "Python", 3.59, 6.9]

# list mutable

a[0] = 10
print(a)
print(a[-1])# last element print korbe
print(len(a))

# s = "Hello World" ---> [H, e, l, l, o,  , W, o, r, l, d]
s = "Hel   lo W  orld"
print(list(s))

# append() method
a.append("new element")
print(a)

# insert() method
a.insert(2, "inserted element")
print(a)

# remove() method
a.remove("rahat")
print(a)

# pop() method
a.pop() # last element remove kore
print(a)

# copy() method
b = a.copy()
print(b)

# clear() method
a.clear()
print(a)

# extend() method
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

# index() method
print(a.index(5)) # element er index number return kore




# tuple immutable

t = (1, 2, 3, "rahat", "Python", 3.59, 6.9)

# t[0] = 10 # error dibe karon tuple immutable
print(t)
print(t[-1])# last element print korbe
print(len(t))

# tuple reverse
print(t[::-1])
