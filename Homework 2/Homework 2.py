import datetime

# Open input and output files
with open('inputDates.txt', 'r') as input_file, open('parsedDates.txt', 'w') as output_file:
    # Get current date
    current_date = datetime.datetime.now()

    # Loop through input file lines
    for line in input_file:
        # Strip line and check for termination condition
        date_str = line.strip()
        if date_str == '-1':
            break

        try:
            # Parse date and check if it's before or on current date
            date = datetime.datetime.strptime(date_str, '%B %d, %Y')
            if date <= current_date:
                # Write parsed date to output file and print to console
                output_file.write(date.strftime('%m/%d/%Y') + '\n')
                print(date.strftime('%m/%d/%Y'))
        except ValueError:
            pass
