def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print(a, b)
    print(b, c)
    print(a, c)
print_params()
#def print_params(b=25, c=[1, 2, 3]):
#    print(print_params)
# print_params()
f = 12
lst = [1, 'two', f]
slr = {1:'цифра', 'строка':'буквы', True:'переменная'}
print_params = (*lst, **slr)
print(print_params)