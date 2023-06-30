def binary_search(arr, price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= price > arr[mid - 1] < price or mid == 0:
        return mid + 1





