my_list = []
my_list = list()
my_list = ['apple', 'orange', 'banana']
fruit = 'apple' in my_list #оператор in возврвщает буллев тип данных
print(fruit)

my_list.reverse()# переворачивает все элементы
print(my_list)

reversed_list = reversed(my_list)
print(list(reversed_list))

print(my_list)

my_list.sort(key=lambda x : x[-1]) # sort cортирует, способ сортировки можно задать с помощью key
print(my_list)


my_list.append('mango') # добавляет элемент на пол=следнее место

my_list.insert(0, 'cherry') #insert ставит что то на указанный индекс(вставляет)


my_list.remove('apple') # удаляет конкретный указанный элемент(если нет = ошибка)

my_list.pop(0) # удаляет и сохраняет элемент по индексу (если индекс не указан, то удаляет последний)

my_list.clear() # полностью очищает от всех элементов
print(my_list)


new_list = [0] * 5 # создает списки (связные)
print(new_list)

comp_list = [i for i in range(5)]
print(comp_list)

double_list = [i * 2 for i in range(5)]
print(double_list)



my_tuple = 'x', 'y', 'r'

my_tuple = ('x', 'y', 'r')

my_tuple = tuple('apple')
print(my_tuple)

my_tuple.count('p') # считает количество заданных символов

my_tuple.index('p') # определяет индекс первого заданного элемента

my_tuple = (1, 2, 3, 4, 5, 6)
first, *rest, last = my_tuple # переменная со звездочкой сохраняет список, состоящий из недостоющих элементов 
print(first)
print(rest)
print(last)

my_dict = {'key_1': 1, 'key_2': 2} # словари для смыслового хранения
my_dict = dict(key_1=1, key_2=2)

value = my_dict['key_1'] # мы можем сохранять ключи из словарей
my_dict['new_key'] = 3 # можем перезаписывать переменные

del my_dict['key_1'] # удаляет значение

removed_value = my_dict.pop('key_2') # удаляет и возвращает значение

last_value = my_dict.popitem() # возвращает и удаляет последнее значение 

for k in my_dict.keys():
    print(k)
    
for v in my_dict.values():
    print(v)
    
for k, v in my_dict.items(): 
    print(k, v)
# other_list = my_list.copy()
# other_list[0] = 4
# print(my_list[0])
#                             # тк делимые обьекты связаные, то мы используем copy чтобы при изменении одного не менялся другой обьект
other_dict = my_dict.copy()
# other_dict['key_1'] = 4
# print(my_dict['key_1'])



my_set = {1, 1, 2, 2} # создание множества
print(my_set)

unique = set('arnold swh')
print(unique)

my_set = {1, 2}
my_set.add(3)
print(my_set)

my_set.remove(3) # удаляет элемент, если его нет то ошибка
print(my_set)

my_set.discard(3) # удаляет элемент, если его нет то ошибка замалчивается
my_set.discard(2)
print(my_set)


evens = {2, 8, 10}
odds = {1, 3, 7}
primes = {2, 3, 5}

union = evens.union(odds) # обьединяет два множества
print(union)

intersection = evens.intersection(primes)
print(intersection)

my_string = 'Hello \'world\' \\'
print(my_string)

my_string = '   world   '
no_spaces = my_string.strip() # убирает в строке лишние пробелы
print(no_spaces)

to_list = my_string.split()
print(to_list)

first_string = 'Hello world'
second_string = 'Display beautifully'
collection = [first_string, second_string]

for s in collection:
    print(s.rjust(20, '#'))

for s in collection:
    print(s.ljust(20, '#'))
    
some_data = [('banana', 5), ('potato', 2), ('tomato', 15)]

for veg, price in some_data:
    print(f'name: {veg:<10} price: {price:03d}$')
    
from datetime import datetime
today = "Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now())
print(today)

my_string = 'Hello world!'

my_string.startswith('Hello') #возврвщает булев тип данных в зависимости от соответствия подстроки со строкой/словом в самом тексте
my_string.endswith('world')

replased = my_string.replace('Hello', 'Bye bye') # replase заменяет в строке первую введенную подстроку на вторую
print(replased)

some_iteribal = ['a', 'b', 'c']

my_string = ' '.join(some_iteribal) # join позволяет преобразовывать в строку 
print(my_string)

unsorted_list = [(10, -1), (5, 12), (-5, 2)]

sorted_list = sorted(unsorted_list, key=lambda x: x[0])
print(sorted_list)

sorted_list = sorted(unsorted_list, key=lambda x: x[1])
print(sorted_list)

my_list = [1, 2, 3, 4, 5, '6']
convert_list = list(map(lambda x: int(x), my_list))
print(convert_list)

filter_list = list(filter(lambda x: type(x) is str, my_list))
print(filter_list)

from functools import reduce
my_list = [1, 2, 3, 4, 5]

reduced_list = reduce(lambda x, y: x + y, my_list)
print(reduced_list)

only_evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(only_evens)

def my_func(a, b, c):
    print(a, b, c)
    
my_func('Hello', 'World', '!!!')

my_func(a='first', b='second', c='third')
my_func(b='second', c='second', a='first')

my_func('first', b='second', c='third')     

def my_func(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
    
my_func(1, 2, 3, 4, 5, foo = 6, bar = 7)

def my_func(a, b, c):
    print(a, b, c)
    
some_dict = {'a': 1, 'b': 2, 'c': 3}
my_func(**some_dict)


def decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

@decorator
def print_name():
    print('Mike')

print_name()

def square_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

@square_decorator
def add_some(x):
    return x + 5

print(add_some(10))

def repeater (times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeater(times=3)
def say_hello():
    print('Hello, world!')
    
say_hello()

def check_permission(func):
    def wrapper(*args, **kwargs):
        arguments = args[0]
        user = args[1]
        if user == 'admin':
            return func(arguments, user)
        else:
            return 'Denied'
    return wrapper

@check_permission
def extraordinary_function(argument, user):
    return argument + 10 if user else argument - 10
user = 'admin'
print(extraordinary_function(15, user))

from collections import Counter # можно изучить print(dir(Counter))

my_string = 'aaaabbccccbbbb'

my_counter = Counter(my_string)
print(my_counter)


my_list = ['a', 'b', 'c']
for i in enumerate(my_list):
    print(i[0],i[1])