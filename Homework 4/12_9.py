# Marco Lopez
# 1537013

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        # The following line may throw ValueError exception if the input is not a valid integer
        age = int(parts[1]) + 1
    except ValueError:  # Catch the ValueError exception
        age = 0  # Set the age to 0 if the input is not a valid integer

    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
