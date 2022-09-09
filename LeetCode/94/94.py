# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    ans = []
    self.inorder(root, ans)
    return ans
  
  def inorder(self, root: Optional[TreeNode], answer: list[int]) -> None:
    if root == None: return
    
    self.inorder(root.left, answer)
    answer.append(root.val)
    self.inorder(root.right, answer)