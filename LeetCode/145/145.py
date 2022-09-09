# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    ans = []
    self.postorder(root, ans)
    return ans
  
  def postorder(self, root: Optional[TreeNode], answer: list[int]):
    if root == None: return
    
    self.postorder(root.left, answer)
    self.postorder(root.right, answer)
    answer.append(root.val)