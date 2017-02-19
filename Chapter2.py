class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        if self.head is None:
            return "LinkedList []"
        else:
            i = self.head
            vl = [str(i.value)]
            while i.next is not None:
                vl.append(str(i.next.value))
                i = i.next
            return "LinkedList [" + ' -> '.join(vl) +  "]"
    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def delNode(self, value):
        i = self.head
        if i.value == value:
            self.head = i.next
        else:
            while i.next is not None:
                if i.next.value == value:
                    i.next = i.next.next
                    if i.next is None:
                        self.tail = i
                    break
                i = i.next

import random
def randomLinkedList(length, min, max):
    ll = LinkedList()
    for _ in range(length):
        ll.addNode(random.randint(min,max))
    return ll

# 2.1
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

def rm_dup(ll):
    i = ll.head
    if i is not None:
        ll_values = {i.value}
        while i.next is not None:
            if i.next.value in ll_values:
                i.next = i.next.next
                if i.next is None:
                    ll.tail = i
            else:
                ll_values.add(i.next.value)
                i = i.next

def rm_dup_no_tmp(ll):
    i = ll.head
    if i is not None:
        while i.next is not None:
            j = i
            while j.next is not None:
                if i.value == j.next.value:
                    j.next = j.next.next
                    if j.next is None:
                        ll.tail = j
                else:
                    j = j.next
            if i.next is not None:
                i = i.next

ll = randomLinkedList(10,0,4)
print(ll)
rm_dup(ll)
print(ll)
ll = randomLinkedList(10,0,4)
print(ll)
rm_dup_no_tmp(ll)
print(ll)

# 2.2 
# Implement an algorithm to find the nth to last element of a singly linked list.
            
def find_nth(ll, n):
    i = ll.head
    ll_list = list()
    while i is not None:
        ll_list.append(i.value)
        i = i.next
    return ll_list[-n]

ll = randomLinkedList(10,0,10)
print(ll)
find_nth(ll,3)

# 2.3
# Implement an algorithm to delete a node in the middle of a single linked list, given 
# only access to that node.
# EXAMPLE
# Input: the node ‘c’ from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a->b->d->e

def delete_node(n):
    n.value = n.next.value
    n.next = n.next.next

ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.addNode(5)
C = ll.head.next.next
print(ll)
delete_node(C)
print(ll)

# 2.4
# You have two numbers represented by a linked list, where each node contains a single 
# digit. The digits are stored in reverse order, such that the 1’s digit is at the head of 
# the list. Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
# Output: 8 -> 0 -> 8

def add_ll(ll1, ll2):
    def ll_to_int(ll):
        i = ll.head
        ll_list = list()
        while i is not None:
            ll_list.append(i.value)
            i = i.next
        return int(''.join(map(str,reversed(ll_list))))
    def int_to_ll(i):
        ll_list = list(reversed(list(map(int,str(i)))))
        ll = LinkedList()
        for i in ll_list:
            ll.addNode(i)
        return ll
    return int_to_ll(ll_to_int(ll1)+ll_to_int(ll2))

ll1 = LinkedList()
ll1.addNode(3)
ll1.addNode(1)
ll1.addNode(5)
ll2 = LinkedList()
ll2.addNode(5)
ll2.addNode(9)
ll2.addNode(2)
print(add_ll(ll1,ll2))

# 2.5
# Given a circular linked list, implement an algorithm which returns node at the beginning 
# of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an 
# earlier node, so as to make a loop in the linked list.
# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the same C as earlier]
# output: C

def find_circ_ll(ll_head):
    node_list = []
    i = ll_head
    while i is not None:
        if i in node_list:
            return i
        else:
            node_list.append(i)
            i = i.next

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
A.next = B
B.next = C
C.next = D
D.next = E
E.next = C
print(find_circ_ll(A))
