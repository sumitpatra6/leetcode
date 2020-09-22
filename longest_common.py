class Solution:
    def maxSubArray(self, nums):
        max_sum = 0
        max_till_now = nums[
        for i in words:
            max_till_now += i
            if max_till_now < 0:
                max_till_now = 0
            if max_till_now >= max_sum:
                max_sum = max_till_now
            
        return max_sum
        
        
words = [4, -1, 2, 1]
sol = Solution()
print(sol.maxSubArray(words))