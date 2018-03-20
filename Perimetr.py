units = ("мм", "см", "м", "км")
print("Выберите единицу измерения площади прямоугольника:\n")
i = 1
for x in units: print("введите {} для выбора {}".format(i, x)); i += 1
print("\nОжидание ответа...") 
selected_unit = int(input())
while (selected_unit < 0 or selected_unit > 4):
    print("\nВведены неверные данные. Значение должно быть от 1 до {}.".format(len(units)))
    print("Введите заново: ")
    selected_unit = int(input())
print("\nВведите значение сторон прямоугольника:")
a = float(input())
b = float(input())
print("\nПериметр прямоугольника: {} {}".format((a + b) * 2, units[selected_unit - 1]))
