# Marco Lopez
# 1537013

def selection_sort_descend_trace(numbers):
    n = len(numbers)

    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_index]:
                max_index = j

        # Swap the found maximum element with the element at index i
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

        # Output the list after each iteration of the outer loop
        print(" ".join(str(x) for x in numbers) + " ")


if __name__ == "__main__":
    # Read in the list of integers and split them into a list
    numbers = list(map(int, input().split()))

    # Call the selection_sort_descend_trace() function to sort the list
    selection_sort_descend_trace(numbers)
