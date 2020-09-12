''' swapping '''

print('-- swapping using 3rd variable ---')
a = 10
b = 20
print('-- Before swapping -- a: {} b: {}'.format(a, b))
temp = a
a = b
b = temp
print('-- After swapping -- a: {} b: {}'.format(a, b))

print('--' * 20)

print('-- swapping using 3rd variable ---')
c = 28
d = 9
print('-- Before swapping -- c: {} d: {}'.format(c, d))
c = c + d
d = c - d
c = c - d
print('-- After swapping -- c: {} d: {}'.format(c, d))


