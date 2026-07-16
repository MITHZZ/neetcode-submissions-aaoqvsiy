# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue = deque()

        queue.append((1,root))

        res = []
        leveldic = {}


        while queue :
            level,root = queue.popleft()
            if level in leveldic:
                leveldic[level].append(root.val)
            else :  
                leveldic[level] = [root.val]
            
            if root.left : 
                queue.append((level+1,root.left))
            if root.right:
                queue.append((level+1,root.right))

        for key,val in leveldic.items():
            res.append(val)
        
        return res
        
            
 







        