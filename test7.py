''' 
This program counts the number of days Wednesday for the specified period.
'''

import datetime

# Time period for calculation.
beginning = datetime.date(2019, 3, 15)
end = datetime.date(2019, 4, 5)

''' 
Since the day of the beginning of the countdown is Friday,
then we will add 2 days. 7 days a week.
''' 
print(((end - beginning).days + 2) // 7)
