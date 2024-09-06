def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
# распаковка параметров
values_list = [2, 'строчка', True]
values_dict = {'a' : 100, 'b' : 'текст','c' : False}

def print_params(*args, **kwargs):
    for value in args:
        print(value)
    for key, value in kwargs.items():
        print(key, ':', value)

print_params(*values_list, **values_dict)
#распаковка плюс отдельные параметры
values_list_2 = [54.21, 'строка']
print_params(*values_list_2, 42)


