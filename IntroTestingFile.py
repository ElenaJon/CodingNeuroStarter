age = 42
first_name = 'Elena'
print(first_name + ' is ' + str(age) + ' years old.')
number_of_rounds = 0
for i in range(age):
    number_of_rounds += 2
print(first_name + ' has lived through ' + str(number_of_rounds) + ' rounds')
#swap variables
x = 1
y = 2
swap = x
x = y
y = swap
print('x is ', x, ' and y is ', y)
#slicing
cell_name = 'neuron'
print(cell_name[1:99])

import datetime
start_of_year = datetime.date.fromisoformat('2025-01-01')
this_day = datetime.date.today()
test_day = datetime.date.fromisoformat('2025-01-02')
print("Today is", datetime.date.today())
print(type(start_of_year), "and", type(this_day))
day_of_year = this_day - start_of_year + datetime.timedelta(days=1)
test_day_of_year = test_day - start_of_year + datetime.timedelta(days=1)
print("Today is the ", day_of_year.days, "day of the year")
print("Tast day is the ", test_day_of_year.days, "day of the year")

#lists
life_exp = [48.1, 56.6, 64.0, 71.0, 75.2, 79.2, 82.3]
life_exp_2000s = [82.3, 85.1, 87.3, 89.5, 91.6, 91.6]

print('With duplicated values:', life_exp)
life_exp.pop(-1)
print('Removed duplicate value:', life_exp)
print(life_exp[0:20])
print(life_exp[-1:3])

#dictionary
weekdays = {'Monday': 1,
            'Tuesday': 2,
            'Wednesday': 3,
            'Thursday': 4,
            'Friday': 5}
print(weekdays['Wednesday'])
weekdays.update({'Saturday': 6, 'Sunday': 7})
weekdays.pop('Wednesday')
print(weekdays)

#for loops
colors = ['red', 'green', 'blue']
color_codes = []
for color in colors:
    color_codes.append(color[0].upper())
print(color_codes)