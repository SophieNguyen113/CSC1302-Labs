# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    index = binary_search(arr, x)
    if index == -1:
        print(f"{x} is NOT present in array.")
    else:
        print(f"{x} is present at index {index}.")
        


