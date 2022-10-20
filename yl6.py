a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a > b and a > c:
    print('max:', a)
elif b > c:
    print('max:', b)
else:
    print('max:', c)
