def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr):
    for i in arr:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr


def filter_and_sort_evens(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    bubble_sort(result)
    return result


# Note : i used bubble sort to sort the final array
# to demonstrate a manual implementation of sorting,
# a much better way would be to use the build in sort() function
# that is much faster than bubble sort.
# Bubble sort has O(n^2) time complexity,
# while the built in sort() function has a time complexity of O(n log n)
# which means using sort() would be faster (much much much faster)
# and also simpler than implementing a slower sorting algorithm
# The function below outputs the exact same thing except it is much simpler and faster
# def filter_and_sort_evens(numbers):
#    result = []
#    for i in numbers:
#        if i % 2 == 0:
#            result.append(i)
#    result.sort()
#    return result


def count_character_frequency(text):
    text = text.replace(" ", "").lower()
    char_set = set(text)
    char_dict = dict.fromkeys(char_set, 0)
    for key in char_dict:
        for i in range(len(text)):
            if key == text[i]:
                char_dict[key] = char_dict[key] + 1
    return char_dict


print(filter_and_sort_evens([3, 1, 4, 7, 1, 5, 9, 2, 6, 8]))
print("\n")

character_count = count_character_frequency(
    "This my task for Basic Data Structures & Algorithms"
)

for key, value in character_count.items():
    print(f"Character: {key} Count: {value}")
