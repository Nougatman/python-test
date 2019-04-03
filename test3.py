t = 12345, 54321, 'hello!'
print (t[0], "\n")
print (t, "\n")
u = t, (1, 'zzz', 42, 1314)
print (u, "\n")
u_1 = t, u
print (u_1, "\n")

empty = ()
singleton = 'Hello'
print (len(empty), "\n")
print (len(singleton), "\n")
print (singleton, "\n")

x, y, z = t
print (x, "\n", y, "\n", z, "\n")

t_1 = [10, 20, 30, 40]
u_2 = [111, 234, 225, 12, -14, 2, -134, 6]
k = t_1 + u_2
print ("Объединяем списки t_1 и u_2:\n", k)
print ("Отсортируем получившийся список по возрастанию:\n", sorted(k))
print ("Отсортируем получившийся список по убыванию:\n", sorted(k, reverse = True))
