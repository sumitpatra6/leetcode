class Solution:
    def moveZeros(self, nums):
        length = len(nums)
        i = 0
        print(nums)
        while i < length:
            print(i, length)
            if nums[i] == 0:
                print(i, length)
                nums[i:length - 1] = nums[i+1:length]               
                nums[length - 1] = 0
                print(nums)
                length = length - 1
                if nums[i] == 0:
                    continue
                else:
                    i+=1
            else:
                i+= 1
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                print(i, length)
                nums[i:length - 1] = nums[i+1:length]
                print(nums)
                nums[length - 1] = 0
        """
        return nums


def moveZeros(nums):
    lastNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZero] = nums[i]
            lastNonZero += 1
    print(nums)
    for i in range(lastNonZero, len(nums)):
        nums[i] = 0
    return nums

nums = [0,1,0,3,12]
sol = Solution()
print(sol.moveZeros(nums))


nums = [0,0 , 1]
sol = Solution()
print(sol.moveZeros(nums))
nums = [0,1,0,3,12]
print('------')
print(moveZeros(nums))