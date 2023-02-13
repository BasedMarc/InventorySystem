print("Birthday Calculator")
print("Current Day")

current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))

print("Birthday")

birthday_month = int(input("Month: "))
birthday_day = int(input("Day:"))
birthday_year = int(input("Year: "))

current_age = int

if (current_month == birthday_month) and (current_day == birthday_day):
    current_age = (current_year - birthday_year)
    print('You are', current_age, ' years old.')
    print('Happy Birthday!')

else:
    current_age = current_year - birthday_year
    print('You are', current_age, ' years old.')
