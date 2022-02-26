class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, node):
        temp = self.head
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return
        while temp.next:
            temp = temp.next
        temp.next = node
        self.tail = node
        node.prev = temp
        self.length += 1
    
    def remove(self, val):
        temp = self.head
        if temp.val == val:
            self.head = temp.next
            return
        while temp.next:
            if temp.next.val == val:
                if temp.next.next:
                    temp.next.next.prev = temp
                else:
                    self.tail = temp
                temp.next = temp.next.next
                self.length -= 1
                break
            temp = temp.next

    def empty_list(self):
        temp = self.head
        while temp:
            next = temp.next 
            del temp 
            temp = next
        self.tail = None
        self.head = None 
        self.length = 0

    def print_list_forward(self):
        temp = self.head 
        while temp:
            print(temp.val)
            temp = temp.next

    def print_list_backward(self):
        temp = self.tail
        while temp:
            print(temp.val)
            temp = temp.prev

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(Node(5))
    ll.append(Node(-1))
    ll.append(Node(3))

    # ll.remove(3)
    ll.print_list_forward()
    ll.print_list_backward()
