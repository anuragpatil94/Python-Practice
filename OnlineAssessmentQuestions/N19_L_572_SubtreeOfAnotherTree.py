


# IMPORTANT - How I approached recursive vs how it should be approached. Since we have to return result and still want to go through all recursion we use `and` `or` in between 2 recursions.e

# My SOlution Not Working.
# class Solution:
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         return self._isSubtree(s,t,0)
    
#     def _isSubtree(self,node,t,found):
#         if not node: 
#             if not t:
#                 return 1
#             else:
#                 return 0
            
        
#         if node.val == t.val:
#             found = 1
#             found = self._isSubtree(node.left,t.left, found)
#             found = self._isSubtree(node.right,t.right,found)
#         else:
#             found = 0
#         if found:
#             return 1
#         self._isSubtree(node.left,t, found)
#         self._isSubtree(node.right,t,found)
#         return found

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s, t) :
        return self.traverse(s,t)
    
    def equal(self,s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.equal(s.left, t.left) and self.equal(s.right,t.right)
    
    def traverse(self,s,t):
        return (s and (self.equal(s,t) or self.traverse(s.left,t) or self.traverse(s.right,t)))


    
    def isSubtree2(self, s, t):
        def sub(s, t, started=False):
            if not s: return not t
            if not t: return not s
            if s.val != t.val:
                if started: return False
                return sub(s.left,t,started) or sub(s.right,t,started)
            if s.val == t.val:
                return (sub(s.left,t.left,1) and sub(s.right,t.right,1)) or (sub(s.left,t,0) or sub(s.right,t,0))
            return False
        return sub(s, t)