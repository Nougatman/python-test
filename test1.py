matrix = [
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [100, 200, 300, 400],
    [1000, 2000, 3000, 4000],
]

print (matrix)
print ("\nWell done?\n")

matrix_1 = [[row[i] for row in matrix] for i in range(4)]

print (matrix_1, "\n")

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print (transposed, "\n")
    
    # bad method!
print (list(zip(*matrix)))
k = []
for i in range(100):
    k.append(i)
print ("\n", k, "\n")
k_1 =[]
for i in range(len(k)):
    if (i % 2 ==0):
        k_1.append(i * 2)
print ("Вывод нового списка, состоявшего из кватрадов тех элементов списка k, что являются четными\n", k_1)
k_1 = k_1[::3]
print ("Удалим из получившегося списка каждый третий элемент:\n", k_1)
