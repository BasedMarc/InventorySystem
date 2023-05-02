# Marco Lopez
# 1537013

# Function to get the age from the user and validate it
def get_age():
    age = int(input())  # Read the age from the user input
    if age < 18 or age > 75:  # Check if the age is within the valid range
        raise ValueError("Invalid age.")  # Raise an exception for invalid ages
    return age  # Return the age if it is valid


# Function to calculate the fat burning heart rate based on the given age
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.7  # Calculate the fat burning heart rate (70% of (220 - age))
    return heart_rate  # Return the calculated heart rate


# Main section of the code
if __name__ == "__main__":
    try:
        age = get_age()  # Call the get_age() function to read and validate the age
        heart_rate = fat_burning_heart_rate(
            age)  # Call the fat_burning_heart_rate() function to calculate the heart rate
        # Print the result
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
    except ValueError as e:  # Handle the exception if the age is not valid
        print(f"{e}\nCould not calculate heart rate info.\n")  # Print the error message and additional information
