my_dict = {'Natasha': 1997, 'Ivan': 1991, 'Mary': 2014}
print(my_dict)
print(my_dict['Natasha'])
print(my_dict.get('Vova'))
my_dict.update({'Sasha': 1992, 'Ilya': 1987})
www = my_dict.pop('Ivan')
print(www)
print(my_dict)

my_set = {10, 11, 12, 'K&B', 12, 11, 10}
print(my_set)
print(my_set.add('Egypt'))
print(my_set.add(2024))
print(my_set.remove(10))
print(my_set)