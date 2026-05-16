class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            value = stones.pop() - stones.pop()
            if value:
                stones.append(value)


        return stones[0] if stones else 0