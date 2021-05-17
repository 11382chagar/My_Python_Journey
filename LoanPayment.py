IR = float(input('What s the annual interest rate? '))
term = float(input('What is the term of the loan in years? '))
amount = float(input('How much is the loan? '))
monthly_payment = amount*IR/(1-1/(1+IR)**(term*12))
total_payment = monthly_payment*term*12
print(monthly_payment)
print(total_payment)