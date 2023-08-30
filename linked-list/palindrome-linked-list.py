'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Test Cases:
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_pointer = head

        def recursive_check(curr: ListNode) -> bool:
            if curr:
                if not recursive_check(curr.next):
                    return False
                if self.front_pointer.val != curr.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursive_check(head)



        
