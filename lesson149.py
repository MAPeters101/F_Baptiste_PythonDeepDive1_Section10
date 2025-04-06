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




