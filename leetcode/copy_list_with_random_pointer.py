class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        sourceListNodeToIx = {}
        ixToSourceListNode = {}
        newNodesValues = []
    
        ix = 0
        while head:
            sourceListNodeToIx.update({head: ix})
            ixToSourceListNode.update({ix: head})
            newNodesValues.append(head.val)
            if head.random != None:



            head = head.next
            ix += 1

if __name__ == '__main__':
    head = createLinkedList([7,None],[13,0],[11,4],[10,2],[1,0])

    s = Solution()
    print(s.copyRandomList())  # 62