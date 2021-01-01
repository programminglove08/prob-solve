#linked-list
#https://leetcode.com/problems/reverse-linked-list-ii/
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        if (m==n):
            return head

        current = head
        prev = None
        loop = 1
        while(loop < m):
            prev = current
            current = current.next
            loop += 1
    
        con = prev
        tail = current
        while(loop <= n):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            loop +=1

        if con: con.next = prev
        else: head = prev
        tail.next = current
        return head
                
        