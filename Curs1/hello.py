def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped, the array is sorted
        if not swapped:
            break
    return arr

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)
