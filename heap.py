# For an array representation of a heap, a node's children can be found at a[n] = a[2n+1] and a[2n+2] (zero-based)
# This means the root or a node a[n] is a[(n-1)//2]

# Heap is always a complete binary tree - meaning that all of the elements of the tree are filled except the deepest
# layer, which is filled from left to right

from re import L


class Heap:
    def __init__(self):
        self.lookup = {}
        self.container = []
        self.size = 0
    
    # To insert, put the node in the next free space to make a complete binary tree. 
    # Then, compare its value with the root, and if necessary swap the two nodes. Repeat.
    def insert(self, val):
        self.container.append(val)
        if val in self.lookup:
            self.lookup[val].append(self.size)
        else:
            self.lookup[val] = [self.size]
        self.size += 1
        self.bubble_up(self.size - 1, val)

    # Used to insert elements. We insert at the next available node, then look upward,
    # swapping elements with the root as needed
    def bubble_up(self, idx, val):
        root_idx = (idx-1)//2
        if root_idx >= 0 and self.container[idx] < self.container[root_idx]:
            self.swap(root_idx, idx)
            self.bubble_up(root_idx, val)

    def bubble_down(self, idx):
        l_idx = (2*idx) + 1
        r_idx = (2*idx) + 2
        if r_idx < self.size and l_idx >= 0:
            l_value = self.container[l_idx]
            r_value = self.container[r_idx]
            if self.container[idx] > l_value or self.container[idx] > r_value:
                if l_value > r_value:
                    self.swap(r_idx, idx)
                    self.bubble_down(r_idx)
                else:
                    self.swap(l_idx, idx)
                    self.bubble_down(l_idx)

    def print_heap(self):
        print(self.container)
        print(self.lookup)

    def swap(self, i, j):
        self.lookup[self.container[i]].remove(i)
        self.lookup[self.container[j]].remove(j)
        self.lookup[self.container[i]].append(j)
        self.lookup[self.container[j]].append(i)
        if not self.lookup[self.container[i]]:
            del self.lookup[self.container[i]]
        if not self.lookup[self.container[j]]:
            del self.lookup[self.container[j]]
        self.container[j], self.container[i] = self.container[i], self.container[j]


    # In the case of duplicates, it doesn't matter which duplicate is removed.
    def remove(self, val):
        idx = self.lookup[val][0]
        if idx == 0:
            self.pop()
            return
        if idx == self.size-1:
            self.container.pop()
            self.lookup[val].pop()
            if not self.lookup[val]:
                del self.lookup[val]
            return
        self.swap(idx, self.size-1)
        self.container.pop()
        self.size -= 1
        self.bubble_down(idx)
        if self.container[idx] == val:
            self.bubble_up(idx, val)

    # Remove the node at the head. Then, replace the head with the most recently added
    # node in the heap. 
    def pop(self):
        if self.size > 0:
            self.swap(0, self.size-1)
            self.container.pop()
            self.size -= 1
            self.bubble_down(0)

h = Heap()
h.insert(5)
h.insert(6)
h.insert(3)
h.insert(1)
h.insert(7)
h.insert(4)
h.insert(2)
# h.pop()
h.remove(2)
h.remove(1)
h.print_heap()