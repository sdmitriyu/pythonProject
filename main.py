def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print(a, b)
    print(b, c)
    print(a, c)

print_params()

def print_params(b=25, c=[1, 2, 3]):
    print(b, c)

print_params()

lst = [1, 'строка', True]
slr = {'a': 1, 'b': 'строка', 'c': True}
print_params(*lst)
print_params(**slr)