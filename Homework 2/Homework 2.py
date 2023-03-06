import datetime
# Get the current date and time
current_date = datetime.datetime.now()
# Continuously ask for user input until -1 is entered
while True:
    date_str = input().strip()
    if date_str == '-1':
        break

    try:
        # Attempt to convert the user input into a datetime object using the specified format
        date = datetime.datetime.strptime(date_str, '%B %d, %Y')
        # Check if the input date is earlier than or equal to the current date
        if date <= current_date:
            # Print the formatted date if it meets the criteria
            print(date.strftime('%m/%d/%Y'))
    except ValueError:
        # If the user input cannot be converted to a datetime object, ignore it
        pass
