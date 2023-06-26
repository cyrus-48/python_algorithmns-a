def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target if found
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Return -1 if the target is not found

# Example usage:
numbers = [1, 2, 4, 5, 7, 9]
target_number = 7
result = binary_search(numbers, target_number)
if result != -1:
    print(f"Target number {target_number} found at index {result}")
else:
    print(f"Target number {target_number} not found")
