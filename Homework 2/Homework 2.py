import datetime

current_date = datetime.datetime.now()

while True:
    date_str = input().strip()
    if date_str == '-1':
        break

    try:
        date = datetime.datetime.strptime(date_str, '%B %d, %Y')
        if date <= current_date:
            print(date.strftime('%m/%d/%Y'))
    except ValueError:
        pass
