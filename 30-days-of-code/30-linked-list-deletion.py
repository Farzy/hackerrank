class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    @staticmethod
    def insert(head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    @staticmethod
    def display(head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    @staticmethod
    def remove_duplicates(head):
        start = head
        while start is not None:
            data = start.data
            next_node = start.next
            while next_node is not None and next_node.data == data:
                next_node = next_node.next
            start.next = next_node

            start = start.next
        return head


# Write your code here

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.remove_duplicates(head)
mylist.display(head)
