class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        
        queue = deque([("0000", 0)])
        visited = {"0000"}
        
        while queue:
            curr, turns = queue.popleft()
            if curr == target:
                return turns
            
            for i in range(4):
                digit = int(curr[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    next_state = curr[:i] + str(new_digit) + curr[i+1:]
                    
                    if next_state not in dead_set and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
        
        return -1