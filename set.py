# empty_set = set()                       create empty set

numbers = {1, 2, 3}

# numbers.add(4)                          {1, 2, 3, 4}   
# numbers.remove(3)                       {1, 2}
# numbers.remove(5)                       KeyError

# numbers.discard(2)                      {1, 3}
# numbers.discard(5)                      {1, 2, 3}

# print(numbers)


# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a.intersection(b))                {3}
# print(a & b)                            {3}

# print(a.difference(b))                  {1, 2}
# print(a - b)                            {1, 2}

# print(a.symmetric_difference(b))        {1, 2, 4, 5}
# print(a ^ b)                            {1, 2, 4, 5}

# print(a.union(b))                       {1, 2, 3, 4, 5}
# print(a | b)                            {1, 2, 3, 4, 5}



# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# union = a | b                           Об'єднання множин
# intersection = a & b                    Перетин множин
# difference = a - b                      Різниця множин
# symmetric_difference = a ^ b            Симетрична різниця

# print(union)                            frozenset({1, 2, 3, 4, 5})
# print(intersection)                     frozenset({3})
# print(difference)                       frozenset({1, 2})
# print(symmetric_difference)             frozenset({1, 2, 4, 5})
