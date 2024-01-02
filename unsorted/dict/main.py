m = {'size': 'L', 'color': 'gray', 'test': 'test'}

print(m)

for v in m.values():
    print(v)
    
for i in m.items():
    print(i)
    
for k, v in m.items():
    print('Key: {}, Value: {}'.format(k, str(v)))
    
print('{}'.format(str(m.get('size', 0))))

print('{}'.format(str(m.get('t', 0))))

if 'age' not in m:
    m['age'] = '5'

print(m)

m.setdefault('name', 'tttt')
print(m)

x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
z = {**x, **y}
print(z)
    