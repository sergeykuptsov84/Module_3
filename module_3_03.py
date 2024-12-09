def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

value_list = [2, True, 'strong']
values_dict = {'a': 1, 'b': 'string', 'c': True }
print_params(*value_list)
print_params(**values_dict)

value_list2 = [54.32, 'STRING']
print_params(*value_list2, 42)