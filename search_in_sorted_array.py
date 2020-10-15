def search(nums, target):
    def util(low, hi):
        if low > hi:
            return -1
        mid = int((low + hi) / 2)
        print(mid)
        if target == nums[mid]:
            return mid
        if nums[low] <= nums[mid]:
            # this means that that the left side is sorted
            if nums[low] <= target < nums[mid]:
                return util(low, mid - 1)
            else:
                return util(mid + 1, hi)
        else:
            if  nums[hi] >= target > nums[mid]:
                return util(mid + 1, hi)
            else:
                return util(low, mid -1)
    return util(0, len(nums) - 1)

nums = [3, 1]
target = 1
print(search(nums, target))