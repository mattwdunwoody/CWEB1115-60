print(type(2))
print(type(2.5645))
print(type("hello"))

# string is immutable
a = "test 1"
print(a)
print(id(a))
a = "test 2"
print(a)
print(id(a))

# list is mutable
b = [1, "banana", 345]
print(b)
print(id(b))
b += [100, "second banana"]
print(b)
print(id(b))

# tuples are immutable
c = (1, "banana", 345)
print(c)
print(id(c))
c += (100, "Second banana", 345)
print(c)
print(id(c))

# python reuses memory addresses
d = "Dunwoody"
e = "Dunwoody"
print(id(d))
print(id(e))

d = "Dunwoody"
e = "Dunwoody Technical College"
print(id(d))
print(id(e))