s = {1,2,3}
s = set([4,5,6])
s = {1,1,2,2,3,3,4,4,5,5}
print(s)

# print(s[1]) // err

s.update([6,7,8,9,10,1,2,3,4,5])
print(s)

s.remove(10)
print(s)

s.discard(10)
print(s)

s1 = {'a','b','c'}
s2 = {4,5,6}
mix = s1.union(s2)
print(mix)

print(s.difference(s2))

s3 = {1,2,3}
s4 = {2,3,4}
print(s3.symmetric_difference(s4))