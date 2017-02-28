class BinaryTree:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value) + " ( " + str(self.left) + " | " + str(self.right) + " )"

class DirectedGraph:
    def __init__(self, value):
        self.value = value
        self.neighbors = list()

class Node:
    def __init__(self, contents):
        self.contents = contents
        self.next = None
    def __str__(self):
        return self.contents.__str__()

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        if self.head is None:
            return "ListList: []"
        else:
            i = self.head
            l = [i.__str__()]
            while i.next is not None:
                l.append(i.next.__str__())
                i = i.next
            return "LinkedList: [ " + ' -> '.join(l) +  " ]"
    def addNode(self, contents):
        node = Node(contents)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

# 4.1
# Implement a function to check if a tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
# from the root by more than one.

def tree_balanced(bt):
    def max_depth(bt):
        rd = 0 if bt.right is None else max_depth(bt.right)+1
        ld = 0 if bt.left is None else max_depth(bt.left)+1
        return max(rd, ld)
    def min_depth(bt):
        rd = 0 if bt.right is None else min_depth(bt.right)+1
        ld = 0 if bt.left is None else min_depth(bt.left)+1
        return min(rd, ld)
    return (max_depth(bt) - min_depth(bt)) < 2

bt = BinaryTree(1)
tree_balanced(bt)
bt.left = BinaryTree(2)
bt.left.left = BinaryTree(3)
tree_balanced(bt)
bt.right = BinaryTree(4)
tree_balanced(bt)

# 4.2
# Given a directed graph, design an algorithm to find out whether there is a route between 
# two nodes.

def is_route(start_node, end_node):
    def find_route(start_node, end_node):
        if start_node is end_node:
            return True
        found = list()
        for n in start_node.neighbors:
            if n not in cache:
                cache.append(n)
                found.append(find_route(n, end_node))
        return any(found)
    cache = list()
    return find_route(start_node, end_node)

def bfs_is_route(start_node, end_node):
    cache = list()
    stack = [start_node]
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node is end_node:
            return True
        if current_node not in cache:
            cache.append(current_node)
            for n in current_node.neighbors:
                stack.append(n)
    return False

dg = DirectedGraph(1)
target_node_a = DirectedGraph(99)
target_node_b = DirectedGraph(99)
dg.neighbors = [DirectedGraph(2), DirectedGraph(3), DirectedGraph(4), target_node_a]
is_route(dg, target_node_a)
is_route(dg, target_node_b)
bfs_is_route(dg, target_node_a)
bfs_is_route(dg, target_node_b)
dg.neighbors = [DirectedGraph(2), DirectedGraph(3), DirectedGraph(4)]
dg.neighbors[0].neighbors = [DirectedGraph(2), dg]
dg.neighbors[0].neighbors[0].neighbors = [dg, target_node_a]
is_route(dg, target_node_a)
is_route(dg, target_node_b)
bfs_is_route(dg, target_node_a)
bfs_is_route(dg, target_node_b)

# 4.3
# Given a sorted (increasing order) array, write an algorithm to create a binary tree with 
# minimal height.

def create_bt(sa):
    if len(sa) > 0:
        bt = BinaryTree(sa.pop(0))
        bt.left = create_bt(sa[:len(sa)//2])
        bt.right = create_bt(sa[len(sa)//2:])
        return bt
    return None

bt = create_bt([1,2,3,4,5,6])

# 4.4
# Given a binary search tree, design an algorithm which creates a linked list of all the 
# nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).

def create_ll(bt):
    ll_list = [LinkedList()]
    queue = [(bt, 0)]
    while len(queue) > 0:
        current_node, current_level = queue.pop(0)
        if current_node is not None:
            if current_level > len(ll_list) - 1:
                ll_list.append(LinkedList())
            ll_list[current_level].addNode(current_node)
            queue.append((current_node.left, current_level + 1))
            queue.append((current_node.right, current_level + 1))
    return ll_list

ll = create_ll(create_bt([1,2,3,4,5,6]))

# 4.5
# Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in
# a binary search tree where each node has a link to its parent.

def find_next_node(btwp):
    if btwp.right is None:
        next_node = btwp.parent
        while next_node is not None and next_node.value < btwp.value:
            next_node = next_node.parent
    else:
        next_node = btwp.right
        while next_node.left is not None:
            next_node = next_node.left
    return next_node

btwp = BinaryTree(20)
btwp.left = BinaryTree(8, parent = btwp)
btwp.left.left = BinaryTree(4, parent = btwp.left)
btwp.left.right = BinaryTree(12, parent = btwp.left)
btwp.left.right.left = BinaryTree(10, parent = btwp.left.right)
btwp.left.right.right = BinaryTree(14, parent = btwp.left.right)
btwp.right = BinaryTree(22, parent = btwp)

print(find_next_node(btwp.left))
print(find_next_node(btwp.left.right.left))
print(find_next_node(btwp.left.right.right))

# 4.6
# Design an algorithm and write code to find the first common ancestor of two nodes
# in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not 
# necessarily a binary search tree.

# 4.7
# You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds
# of nodes. Create an algorithm to decide if T2 is a subtree of T1.

# 4.8
# You are given a binary tree in which each node contains a value. Design an algorithm
# to print all paths which sum up to that value. Note that it can be any path in the tree,
# it does not have to start at the root.
