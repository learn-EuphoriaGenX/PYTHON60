my_set = {'apple', 'banana', 'mango', 'mango'}
print(my_set)
#unordered, unchangeable, duplicate not allowed
a = frozenset({'apple', 'banana', 'mango', 'mango'})
# print(a)

print({'a', 'b', 'c', 'd', 'e'}.difference({'a', 'b', 'c', 'd'}))
print({'a', 'b', 'c', 'd', 'e'}.intersection({'a', 'b', 'c', 'd'}))
print({'a','b'} | {'b','c'})
print({'a','b','c'}.symmetric_difference({'b','c','d'}))
print({'a','b'}.issubset({'a','b','c'}))
print({'a','b','c'}.issuperset({'a','b'}))


# oops exception file
