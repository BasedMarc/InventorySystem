# Marco Lopez 1537013
# CIS 2348-17255

def main():
    input_values = input()
    input_list = input_values.split()

    # Convert strings to integers and filter out negative numbers
    integer_list = [int(x) for x in input_list if int(x) >= 0]

    # Sort the non-negative integers in ascending order
    integer_list.sort()

    # Print the sorted non-negative integers separated by spaces
    for num in integer_list:
        print(num, end=" ")


if __name__ == "__main__":
    main()