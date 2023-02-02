user_input = int(input('Enter integer:'))
print('\nYou entered:', user_input)
user_input_squared = user_input * user_input
user_input_cubed = user_input * user_input * user_input
print(user_input, 'squared is', user_input_squared)
print('And', user_input, 'cubed is', user_input_cubed, '!!')
new_integer = int(input('Enter another integer:\n'))
new_integer_add = new_integer + user_input
new_integer_multiply = new_integer * user_input
print(user_input, '*', new_integer, 'is', new_integer_multiply)

