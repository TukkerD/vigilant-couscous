import datetime

x = datetime.datetime.now()

if x.strftime('%p') == 'PM':
    print('Good Night World')

else:
    print('Good Morning World')
