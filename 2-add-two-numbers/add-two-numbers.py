class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
     
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
           
            current.next = ListNode(new_digit)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

def build_linked_list(numbers):
 
    dummy = ListNode()
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def print_linked_list(node):
  
    while node:
        print node.val,  
        node = node.next
    print

l1 = build_linked_list([2, 4, 3])
l2 = build_linked_list([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("Output linked list:")
print_linked_list(result)