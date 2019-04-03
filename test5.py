tel = {'jack': 4098, 'sape': 4139}
print (tel, "\n")
tel['guido'] = 4127
print (tel,"\n")
print (tel['sape'], "\n")
tel['irv'] = 4127
print (tel, "\n")
print (list(tel), "\n")
print (sorted(tel), "\n")
print (dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]), "\n")
print ({x: x**2 for x in (2, 4, 6)}, "\n")
print (dict(sape=4139, guido=4127, jack=4098), "\n\n")

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print (k, v, "\n")

for i, v in enumerate(['tic', 'tac', 'toe']):
    print (i, v)
print ("\n")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print ('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print (i)
print ("\n")

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print (f)
print ("\n")
