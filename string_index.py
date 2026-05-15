a = "this is a string"

print(a[0])  # Output: 't'
print(a[15])  # Output: 'g'
print(a[4])  # Output: 'i'
print(a[len(a)-1])  # Output: 'g'


# maximum index = total length of the string - 1
# = 16 - 1= 15
# print(a[16])  # This will raise an IndexError because the index is out of range

# Last character printing (long method)
print (a[len(a)-1])  # Output: 'g'

# Last character printing (short method)
print(a[-1])  # Output: 'g'

# Negative indexing

b = "Python is great!"
print(b[-1])  # Output: '!'
print(b[-2])  # Output: 't'
print(b[-3])  # Output: 'a'
print(b[-4])  # Output: 'e'
print(b[-5])  # Output: 'r'
print(b[-6])  # Output: 'g'


# String is a immutable data type

print(b[1])
b[1] = 'a'  # This will raise a TypeError because strings are immutable
print(b)


