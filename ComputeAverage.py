CountPositive = 0
CountNegative = 0
Count = 0
Total = 0

num = int(input('Enter an integer, the input ends if it is 0:'))

while num != 0:
    if num > 0:
        CountPositive + 1
    elif num < 0:
        CountNegative + 1

        Total += num
        Count += num

num = int(input('Enter an integer, the input ends if it is 0:'))

if Count == 0:
    print('No numbers entered except 0')
else:
    print('The number of positives is', CountPositive)
    print('The number of negatives is', CountNegative)
    print('The total is', Total)
    print('The average is', round(Total/Count,2))