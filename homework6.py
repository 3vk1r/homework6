my_dict = {'Zakir': 2003, 'Daria': 2004, 'Sasha': 2005}
print(my_dict)
print(my_dict['Zakir'], my_dict.get('Nikita'))
my_dict.update({'Nikita': 2001,
                'Anita': 2006})
lost = my_dict.pop('Sasha')
print(lost)
print(my_dict)

my_set = {1, 2, 'Zakir', 'Urban', 'Urban', 2, 3, 4, 5, 4}
print(my_set)
my_set.add(31.05)
my_set.add((4, 3, 2, 1, 2))
my_set.discard(2)
print(my_set)