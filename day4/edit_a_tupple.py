#tupple are unchangeable to make changes to it we make a list to edit it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)