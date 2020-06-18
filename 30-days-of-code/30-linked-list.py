class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    @staticmethod
    def display(head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    @staticmethod
    def insert(head, data):
        if head is None:
            return Node(data)
        current = head
        next = head.next
        while next:
            current = next
            next = current.next
        current.next = Node(data)
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
