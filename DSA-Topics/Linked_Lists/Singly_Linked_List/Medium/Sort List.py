# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sortLinkedList(head)
    
    
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge case
        if head == None or head.next == None:
            return head
        
        middlePoint = self.findMiddlePoint(head)
        
        # Splitted two linked list
        list1 = head
        list2 = middlePoint.next
        middlePoint.next = None
        
        print(list2.val)
        
        sortedList1 = self.sortLinkedList(list1)
        sortedList2 = self.sortLinkedList(list2)
        
        return self.mergeTwoSortedLinkedList(sortedList1 , sortedList2)
        
    
    # Merges and return the head of two linked list
    def mergeTwoSortedLinkedList(self , l1: Optional[ListNode] , l2: Optional[ListNode] ) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1000000)
        head = dummyNode
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                newNode = ListNode(l1.val)
                dummyNode.next = newNode
                dummyNode = dummyNode.next

                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                dummyNode.next = newNode
                dummyNode = dummyNode.next

                l2 = l2.next
        
        if l2 != None:
            while l2 != None:
                newNode = ListNode(l2.val)
                dummyNode.next = newNode
                dummyNode = dummyNode.next
                l2 = l2.next
            
        if l1 != None:
            while l1 != None:
                newNode = ListNode(l1.val)
                dummyNode.next = newNode
                dummyNode = dummyNode.next
                l1 = l1.next

        return head.next
    
    # Finds the middle point in linked list
    def findMiddlePoint(self , head : Optional[ListNode]):
        
        # Edge case
        if head == None or head.next == None:
            return head
        
        follower = head
        runner = head.next
            
        while runner.next != None and runner.next.next != None:
            runner = runner.next.next
            follower = follower.next
        
        if runner.next != None:
            follower = follower.next
        
        return follower
