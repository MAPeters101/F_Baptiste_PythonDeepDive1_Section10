
def func(**kwargs):
    for item in kwargs.items():
        print(item)

func(b=100, a=200, y='hello', p='python')
print('-'*80)

