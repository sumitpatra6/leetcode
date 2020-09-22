array = [1, 5,3,2,8,7,6,4]
def quick_sort(array):
    if len(array) <= 1:
        return array
    sort(array, 0, len(array) - 1)
    print(array)
    
    
def sort(array, lo, hi):
    if lo < hi:
        pivot = partition(array, lo, hi)
        sort(array, lo, pivot - 1)
        sort(array, pivot + 1, hi)

def partition(array, lo, hi):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i = i +1
    # bring the pivot in the middle
    array[i], array[hi] = array[hi], array[i]
    return i


print(array)
print(quick_sort(array))