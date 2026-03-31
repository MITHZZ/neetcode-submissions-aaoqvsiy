class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        res = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                l1 = len(words[i])
                l2 = len(words[j])

                if l2 >= l1:
                    if words[i] == words[j][:l1] and words[i] == words[j][l2-l1:]:
                        res+=1


        return res