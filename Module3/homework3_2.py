def print_params(a=1, b='stroka', c=True):
    print(a, b, c)


print_params()
print_params(2, 'wade', False)
print_params('car', 7)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [17, 'happy', True]
values_dict = {'a': 5, 'b': 'kareta', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6, 'ne stroka']

print_params(*values_list_2, 42)