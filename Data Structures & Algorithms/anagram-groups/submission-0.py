class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        group = defaultdict(list)


        for val in strs : 
            key = "".join(sorted(val))
            print(key)
            group[key].append(val)

        res = []

        for val in group.values():
            res.append(val)

        return res