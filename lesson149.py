from sys import version_info
print(version_info)

d = {'b': 1, 'a': 2}
print(d.keys())
print(d.values())
print(d.items())
print()

d['x'] = 3
print(d.keys())
print(d.values())
print(d.items())
print()

del d['a']
print(d.keys())
print(d.values())
print(d.items())
print()

d['a'] = 1
print(d.keys())
print(d.values())
print(d.items())
print()

print(d.items())
print(d)
print(d.popitem())
print(d)
print('-'*80)

d1 = {'a':1, 'b':200}
d2 = {'a':100, 'd':300, 'c':400}
print(d1)
print(d2)
print()
d1.update(d2)
print(d1)
print(d2)
print('-'*80)


