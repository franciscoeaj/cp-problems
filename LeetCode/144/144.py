# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    ans = []
    self.preorder(root, ans)
    return ans
  
  def preorder(self, root: Optional[TreeNode], answer: list[int]) -> None:
    if root == None: return
    
    answer.append(root.val)
    self.preorder(root.left, answer)
    self.preorder(root.right, answer)