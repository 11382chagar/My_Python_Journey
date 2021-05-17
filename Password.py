USER = '11382chagar'
PASSWORD = 'CASuals2'
user_attempt = input('Please enter your username ')
password_attempt = input('Please enter your password ')
if password_attempt == PASSWORD and user_attempt == USER:
    print('Access Granted')
else:
    print('Access Denied')