def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(7, 'Глеб', False)
print_params(100, 'Вова')
print_params(b = 'Петя')
print_params(b = 20)
print_params(c = [1, 2, 3])


values_list = [50, 'Семен', False]
values_dict = {'a': 500, 'b': 'Женя', 'c': True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
