my_dict = {'Max': 2003, 'Ivan': 2018,}
print(my_dict['Max'])
my_dict['Alex'] = 2010
my_dict['Liza'] = 2016
my_dict['Kate'] = 2014
del my_dict['Ivan']
print(my_dict['Liza'])
print(my_dict['Kate'])
print(my_dict)

my_set = {"Big", 2, 2, 4, 'Open'}
print(my_set)
my_set.update([1, 6])
print(my_set)
my_set.discard('Open') # так же можно методом .remove()
print(my_set)