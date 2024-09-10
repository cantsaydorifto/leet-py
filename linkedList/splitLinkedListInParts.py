# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getNodes(t: ListNode | None):
    res = []
    while t:
        res.append(t)
        t = t.next
    return res


class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode]:
        nodes = getNodes(head)
        n = len(nodes)
        if k >= n:
            res = [i.val for i in nodes]
            for i in res:
                i.next = None
            return res + [None] * (k - n)
        numberOfExtraNodes = n % k
        numberOfElementsInEachPart = n // k
        j = 0
        res = []
        for _ in range(k):
            if numberOfExtraNodes > 0:
                part_length = numberOfElementsInEachPart + 1
                numberOfExtraNodes -= 1
            else:
                part_length = numberOfElementsInEachPart

            if j < n:
                t = nodes[j]
                current = t
                for _ in range(part_length - 1):
                    current.next = nodes[j + 1]
                    current = current.next
                    j += 1
                current.next = None
                res.append(t)
                j += 1
            else:
                res.append(None)
        return res


list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)

print(Solution().splitListToParts(list, 5))
