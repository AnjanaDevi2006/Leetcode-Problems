class Solution:
    def swapPairs(self, l: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, l)
        prev = dummy

        for _ in range(0, 100, 2):
            if l is None or l.next is None:
                break

            second = l.next

            prev.next = second
            l.next = second.next
            second.next = l

            prev = l
            l = l.next

        return dummy.next
