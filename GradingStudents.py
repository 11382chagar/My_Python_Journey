test_score = int(input('Please enter your test score '))
if test_score >= 90:
    test_score = 'A'
elif test_score >= 80:
    test_score = 'B'
elif test_score >= 70:
    test_score = 'C'
elif test_score >= 60:
    test_score = 'D'
else:
    test_score = 'F'
print('Your grade is', test_score)
