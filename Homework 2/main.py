my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number + 5 for number in my_list if (number >= -1) and (number % 2 == 1) ]
print(new_list)