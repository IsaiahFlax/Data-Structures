from collections import deque
# Binary search trees are a data structure that enforce an ordering over 
# the data they store. That ordering in turn makes it a lot more efficient 
# at searching for a particular piece of data in the tree. 

# This part of the project comprises two days:
# 1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
#    on the BSTNode class.
# 2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
#    on the BSTNode class.
# """
# class BinarySearchTree:

#     def __init__(self):
#         self.root = None
#         self.size = 0

#     def length(self):
#         return self.size

#     def __len__(self):
#         return self.size

#     def __iter__(self):
#         return self.root.__iter__()
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if not self:
            self = BSTNode(value)
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return False
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        else:
            return True
            

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
        
    def iterative_get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current > max_value:
                max_value = current.value
            current = current.right
        return max_value
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #start at the root! 
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
            #add self.value to array
            #print array
            #add children
            #remove already printed values
                        
        d = deque()
        d.append(self)
        while len(d) > 0:
            current = d.popleft()
            print(current.value)
            if current.left:
                d.append(current.left)
            if current.right:
                d.append(current.right)


        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        d = deque()
        d.append(self)
        while len(d) > 0:
            current = d.pop()
            print(current.value)
            if current.left:
                d.append(current.left)
            if current.right:
                d.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft()
        if self.right is not None:
            self.right.pre_order_dft()
        
            

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left is not None:
            self.left.post_order_dft()
        if self.right is not None:
            self.right.post_order_dft()
        print(self.value)

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
bst.dft_print()
print("In order print")
bst.in_order_print()
print("")
print("bft print")
bst.bft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
#bst.in_order_dft()
print("post order")
bst.post_order_dft()  
