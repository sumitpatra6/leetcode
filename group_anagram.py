class Solution:
    def groupAnagrams(self, strs):
        ret = []
        groups = {}
        for s in strs:
            value = ''.join(sorted(s))
            if value not in groups.keys():
                groups[value] = []
            groups[value].append(s)
        for key in groups.keys():
            ret.append(groups[key])
        return ret

inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(inputs))