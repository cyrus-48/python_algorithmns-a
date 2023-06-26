def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Example usage:
numbers = [4, 2, 7, 1, 9, 5]
target_number = 7
result = linear_search(numbers, target_number)
if result != -1:
    print(f"Target number {target_number} found at index {result}")
else:
    print(f"Target number {target_number} not found")
