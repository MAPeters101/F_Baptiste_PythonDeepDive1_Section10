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

d = {'a':1, 'b':2, 'c':3}
print('start: ', d)
d['a'] = d.pop('a')
print('moved a to end:', d)
print('-'*80)

d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start: ', d)
d['c'] = d.pop('c')
print('moved c to end:', d)
for i in range(len(d)-1):
    key = next(iter(d.keys()))
    d[key] = d.pop(key)
print('moved c to front:', d)
print('-'*80)

d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start: ', d)
d.popitem()
print('pop last item:', d)
print('-'*80)

d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start: ', d)
key = list(d.keys())[0]
print(key)
key = next(iter(d.keys()))
print(key)
d.pop(key)
print('after pop first item:', d)
print('-'*80)

"""http://code.activestate.com/recipies/578375/"""

