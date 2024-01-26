capital_city = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokio'}
 
# print(capital_city)                                           {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokio'}
# print(capital_city['Ukraine'])                                Kyiv
# print(capital_city['Kyiv'])                                   error

# capital_city['Ukraine'] = 'Kharkiv'                           {'Ukraine': 'Kharkiv', 'Spain': 'Madrid', 'Japan': 'Tokio'}
# capital_city['Poland'] = 'Warsaw'                             {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokio', 'Poland': 'Warsaw'}
# del capital_city['Ukraine']                                   {'Spain': 'Madrid', 'Japan': 'Tokio'}
# print('Ukraine' in capital_city)                              True
# print('Moskow' in capital_city)                               False

# Ukraine = capital_city.pop('Ukraine')                         {'Spain': 'Madrid', 'Japan': 'Tokio'}
# capital_city.update({'Ukraine':'Kharkiv', 'Poland':'Warsaw'}) {'Ukraine': 'Kharkiv', 'Spain': 'Madrid', 'Japan': 'Tokio', 'Poland': 'Warsaw'}
# capital_city.clear()                                          {}
# capital_city1 = capital_city.copy()                           {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokio'}

# Ukraine = capital_city.get('Ukraine')                         Kyiv
# Poland = capital_city.get("Poland")                           None

# Ukraine = capital_city["Ukraine"]                             Kyiv
# Poland = capital_city["Poland"]                               KeyError: 'Poland'

# print(Ukraine)
# print(Poland)