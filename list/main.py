l = ['cat', 'bat', 'rat', 'elephant']

print(l[-1])

print(l[0:4])

print(l[1:3])

print(l[0:-1])

l2 = l[:]
print(l2)

l2.append('dog')

print(l2)

print([1,2,3] + ['A','B','C'])

print(['x','y','z'] * 3 )

del l2[2]
print(l2)

supplies = ['pens', 'staples', 'flame-throwers', 'binders']
for i, supply in enumerate(supplies):
    print('Index {} in supplies is : {}'.format(str(i), supply))

names = ['P', 'J', 'E']
ages = [6, 33, 44]
for n, a in zip(names, ages):
    print('{} is {} years old'.format(n, a))
    
print('P' in names)

v = ['f', 'o', 'l']

q, w ,e = v
print(q)
print(w)
print(e)

a, b = 'Alice', 'Bob'
a, b = b, a
print(a)

v.insert(1, 'test')
print(v)

v.remove('test')
print(v)

v.sort()
print(v)

v.sort(reverse=True)
print(v)
print(sorted(v))
