print('{} % {} = {}'.format(10, 3, 10%3))
print('{1} % {2} = {0}'.format(10%3, 10, 3))
print('{a} % {b} = {mod}'.format(mod=10%3, a=10, b=3))
print('-'*80)

a = 10
b = 3
print(f'{a} % {b} = {a%b}')
print(F'{a} % {b} = {a%b}')
print()

a = 10 / 3
print(f'{a:0.5f}')
print(f'{10/3 :0.5f}')
print('-'*80)

name = 'Python'
print(f'{name} rocks!')
print('{name} rocks!'.format(name=name))
print('-'*80)

def outer():
    name = 'Python'
    def inner():
        return f'{name} rocks!'
    return inner
print(outer()())
print('-'*80)

sq = lambda x: x**2
a = 10
b = 1
print(f'{sq(a) if b>5 else a}')
b = 10
print(f'{sq(a) if b>5 else a}')
print('-'*80)

a = 10
b = 1
print(f'{(lambda x: x**2)(a) if b>5 else a}')
b = 10
print(f'{(lambda x: x**2)(a) if b>5 else a}')
print('-'*80)


