x, y = map(int, input().split())
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if x == 1:
    print(week[y%7])
else:
    for i in range(1, x):
        y += month[i]
    print(week[y%7])