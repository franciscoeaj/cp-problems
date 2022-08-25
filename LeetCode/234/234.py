# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    nums = []
    while head != None:
      nums.append(head.val)
      head = head.next
    
    mid = int(math.ceil(len(nums) / 2))
    firstHalf = nums[:mid]
    secHalf = nums[mid:]
    if (len(nums) % 2 != 0):
      firstHalf = nums[:mid - 1]
    
    for i in range(len(firstHalf)):    
      if firstHalf[i] != secHalf[-(i+1)]:
        return False
      
    return True