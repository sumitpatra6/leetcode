class Solution:
    def comparewords(self, word1, word2):
        flag = False
        length = min(len(word1), len(word2))
        for i in range(length):
            #print(self.ordered_dict[word2[i]], self.ordered_dict[word1[i]])
            if self.ordered_dict[word2[i]] > self.ordered_dict[word1[i]]:
                flag =  True
                break
            elif self.ordered_dict[word2[i]] < self.ordered_dict[word1[i]]:
                flag = False
                break
                
        return flag
        
                
                
    def isAlienSorted(self, words, order):
        self.ordered_dict = {}
        for i in range(len(order)):
            self.ordered_dict[order[i]] = i
        #print(self.ordered_dict)
        for i in range(len(words) - 1):
            if not self.comparewords(words[i], words[i+1]):
                return False
        return True
                
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

sol = Solution()
print(True)
print(sol.isAlienSorted(words, order))
print("-----")
words = ["iekm","tpnhnbe"]
order = "loxbzapnmstkhijfcuqdewyvrg"
print(False)
print(sol.isAlienSorted(words, order))
print("------")
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(False)
print(sol.isAlienSorted(words, order))

print("------")
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(False)
print(sol.isAlienSorted(words, order))
