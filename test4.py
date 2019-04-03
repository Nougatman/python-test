basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print (basket, "\n")
a = set('abracadabra')
b = set('alacazam')
print (a, "\n")                                 # unique letters in a
print (a - b, "\n")                             # letters in a but not in b
print (a | b, "\n")                             # letters in a or b or both
print (a & b, "\n")                             # letters in both a and b
print (a ^ b)                                   # letters in a or b but not both
