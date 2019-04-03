import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print (filtered_data, "\n")
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
not_null = string1 or string2 or string3
print (not_null, "\n")
