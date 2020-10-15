class Solution:
    def lastStoneWeight(self, stones):
        length = len(stones)
        while length > 1:
            print('----')
            print(length, stones)
            stones = sorted(stones[:length])
            print(stones)
            a1 = stones[-1]
            a2 = stones[-2]
            print(a1, a2)
            if a1 == a2:
                length -= 2
            else:
                stones[-2] = abs(a1 - a2)
                length -= 1
        print(length)
        return sorted(stones[:length])
            



sol = Solution()
array = [2,7,4,1,8,1]
print(sol.lastStoneWeight(array))