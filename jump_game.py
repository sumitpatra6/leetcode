class Solution:
    def canJump(self, nums):
        #this is the dynamic programming solution
        length = len(nums)
        answer = [False]*length
        if length == 0:
            return False
        if length == 1:
            return True
        answer[-1] = True
        for i in range(length -2, -1, -1):
            for j in range(nums[i], 0, -1):
                if i + j < length and answer[i + j] == True:
                    answer[i] = True
                    break
        return answer[0]

    def canJumpRecMax(self,nums):
        length = len(nums)
        if length <= 1:
            return True
        max = nums[0]
        for i in range(length):
            if max <= i and nums[i] == 0:
                return False
            if i + nums[i] > max:
                max = i + nums[i]
            if max >= length -1:
                return True
        return False 

sol = Solution()
nums = [2, 3, 1, 1, 4]
print(True)
print(sol.canJumpRecMax(nums))
print('---')
nums = [3, 2, 1, 0, 4]
print(False)
print(sol.canJumpRecMax(nums))