# Fungsi Partition
def partition(array, start, end):
    pivot = array[end]
    p_index = start
    
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[p_index] = array[p_index], array[i]
            p_index += 1
    
    array[p_index], array[end] = array[end], array[p_index]
    return p_index

# Fungsi Quick Sort
def quick_sort(array, start, end):
    if start < end:
        p_index = partition(array, start, end)
        quick_sort(array, start, p_index - 1)
        quick_sort(array, p_index + 1, end)
        
# Contoh penggunaan
array = [7, 2, 1, 6, 8, 5, 3, 4]
n = len(array)

quick_sort(array, 0, n - 1)
print("Array setelah diurutkan:", array)
a