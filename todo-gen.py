#!/usr/bin/env python
# coding=utf-8

# The starting date is mm - 1, till 31.
# enter the starting day in week.
# eg. 2 --> Tue 1\n Wed 2\n ......
wkday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

if __name__ == '__main__':
    print("enter the starting day in week.\neg. Starting from Thu. Enter: 2 -->\nTue 1\nWed 2\nThu 3\n....\nEnter the starting date:")
    wkdayn = eval(input()) - 1
    wkdayn += 30
    wkdayn %= 7
    for date in range(31, 0, -1):
        print(f'{wkday[wkdayn]} {date}')
        wkdayn -= 1
        wkdayn %= 7


