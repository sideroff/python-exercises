# unpacking works simmilar to how it does in js
a = [1, 2, 3, 4, 5, 6, 7]

# let [x, y, ...rest] = a
[x, y, *rest] = a

print(x, y, rest)
