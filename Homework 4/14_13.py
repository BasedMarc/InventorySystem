# Marco Lopez
# 1537013

# Global variable
num_calls = 0


def partition(user_ids, i, k):
    pivot = user_ids[(i + k) // 2]
    left = i
    right = k

    while left <= right:
        while user_ids[left] < pivot:
            left += 1
        while user_ids[right] > pivot:
            right -= 1
        if left <= right:
            user_ids[left], user_ids[right] = user_ids[right], user_ids[left]
            left += 1
            right -= 1

    return left


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i < k:
        partition_index = partition(user_ids, i, k)
        quicksort(user_ids, i, partition_index - 1)
        quicksort(user_ids, partition_index, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
