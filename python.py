class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def insert(self, data):
        self.head = Node(data, self.head)
        self.length += 1
    def remove_at_index(self, idx):
        dummy = Node(None, self.head)
        prev, curr = dummy, dummy.next
        check_idx = 0
        while curr:
            print(idx, check_idx)
            if idx == check_idx:
                prev.next = curr.next
                curr.next = None
            check_idx += 1
            prev, curr = curr, curr.next
    def iterate(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next
    def search(self, data):
        idx = 0
        node = self.head
        while node:
            if node.data == data: return idx
            node = node.next
            idx += 1
        return -1