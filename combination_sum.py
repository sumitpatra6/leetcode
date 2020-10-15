import copy
class Solution:
    def combinationSum(self, candidates, target):
        final = []

        def util(result, candidates, target, curr_index):
            # print(result)
            if target == 0:
                final.append(copy.copy(sorted(result)))
                return
            if target < 0:
                return
            for i in range(curr_index, len(candidates)):
                result.append(candidates[i])
                util(result, candidates, target - candidates[i], i)
                result.pop(-1)

        util([], candidates, target, 0)
        print(final)
        return final

    def combinationSumDynamic(self, candidates, target):
        result = [[] for _ in range(target+1)]
        print(result)
        for c in candidates:
            for i in range(1, target + 1):
                if i < c:
                    continue
                if i == c:
                    result[i].append([c])
                else:
                    for sol in result[i-c]:
                        result[i].append(sol+[c])
        print(result[target])

candidates = [2,3,6, 7]
target = 7
sol = Solution()
sol.combinationSumDynamic(candidates, target)
