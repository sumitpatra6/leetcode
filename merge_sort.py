def merge_sort_top_down(nums):
    if len(nums) <= 1:
        return nums
    pivot = int(len(nums) / 2)
    list1 = merge_sort_top_down(nums[0:pivot])
    list2 = merge_sort_top_down(nums[pivot:])
    return merge(list1, list2)


def merge(list1, list2):
    l = 0
    r = 0
    ret = []
    while l < len(list1) and r < len(list2):
        if list1[l] <= list2[r]:
            ret.append(list1[l])
            l += 1
        else:
            ret.append(list2[r])
            r += 1
    ret.extend(list1[l:])
    ret.extend(list2[r:])
    return ret




print(merge_sort_top_down([1,5,3,2,8,7,6,4]))
