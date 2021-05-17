year = int(input('What year are you thinking of? '))
leap_year = False

if year % 4 == 0:
    if year % 100 != 0:
        leap_year = True
elif year % 400 == 0:
    leap_year = True
else:
    leap_year = False

if leap_year:
    print('This is a leap year')
else:
    print('This is not a leap year')
