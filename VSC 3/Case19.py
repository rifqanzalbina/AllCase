def closest_zero(arr):
    arr.sort()
    min_diff = float('inf')
    l, r = 0, len(arr) - 1
    while l <= r:
        if abs(arr[l]) < abs(arr[r]):
            min_diff = min(min_diff, abs(arr[l]))
            l += 1
        else:
            min_diff = min(min_diff, abs(arr[r]))
            r -= 1
    return min_diff

print(closest_zero([1, 60, -10, 70, -80, 85]))