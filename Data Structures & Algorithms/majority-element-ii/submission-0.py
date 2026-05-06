class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        thre = len(nums)/3

        freq = {}

        for val in nums:
            freq[val] = freq.get(val,0)+1

        res = []
        for val, freq in freq.items():
            if freq > thre:
                res.append(val)

        return res
