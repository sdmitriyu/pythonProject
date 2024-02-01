def test(*args, **kwargs):
    print(test)
    print('тип args', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр', i, arg)
    print('тип kwargs', type(kwargs))
    print(kwargs)
    for i, kwarg in enumerate(kwargs):
        print('именованный параметр', i, kwarg)


test(1, "hello", [2, 3, 4], {"a": 5, "b": 6})


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1


print(factorial(7))