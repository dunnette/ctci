# 16.1 
# Given a sorted array of positive integers with an empty 
# spot (zero) at the end, insert an element in sorted order.

def insert_into_array(l, t):
    for i in range(len(l)-1):
        if t < l[i]:
            t, l[i] = l[i], t
    l[-1] = t

l = [1, 2, 4, 5, None]
e = 3
insert_into_array(l, e)
assert l == sorted(l)
l = [1, 2, 3, 4, None]
e = 0
insert_into_array(l, e)
assert l == sorted(l)
l = [1, 2, 3, 4, None]
e = 5
insert_into_array(l, e)
assert l == sorted(l)

# 16.2 
# Reverse the order of elements in an array (without creating 
# new array).

def reverse_array(l):
    for ii in range(len(l)//2):
        l[ii], l[-ii-1] = l[-ii-1], l[ii]

l = []
l_static = list(l)
reverse_array(l)
assert l == list(reversed(l_static))
l = [0]
l_static = list(l)
reverse_array(l)
assert l == list(reversed(l_static))
l = [0,1]
l_static = list(l)
reverse_array(l)
assert l == list(reversed(l_static))
l = [0,1,2]
l_static = list(l)
reverse_array(l)
assert l == list(reversed(l_static))

# 16.3 
# Given two lists (A and B) of unique strings, write a 
# program to determine if A is a subset of B. That is, check 
# if all the elements from A are contained in B.

def is_contained(A, B):
    B_set = set(B)
    for s in A:
        if s not in B_set:
            return False
    return True

A = ['one', 'two', 'three']
B = ['two']
assert is_contained(A,B) == False
A = ['one', 'two', 'three']
B = ['two', 'three', 'one']
assert is_contained(A,B) == True
A = ['one', 'two', 'three']
B = ['four', 'one', 'two', 'three']
assert is_contained(A,B) == True

# 16.4 
# You are given a two-dimensional array of sales data where
# the first column is a product ID and the second column is 
# the quantity. Write a function to take this list of data 
# and return a new two-dimensional array with the total sales 
# for each product ID. 

def sales_add(s):
    total_sales = dict()
    for item, sales in s:
        if item in total_sales:
            total_sales[item] += sales
        else:
            total_sales[item] = sales
    return list(map(list,total_sales.items()))

sales_data = [[211, 4], [262, 3], [211, 5], [216, 6]]
sales_add(sales_data)

# 16.5 
# Insert an element into a binary search tree (in order). 
# You may assume that the binary search tree contains 
# integers.

class BSNode:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None

def add_element(n, v):
    if v < n.content:
        if n.left is None:
            n.left = BSNode(v)
        else:
            add_element(n.left,v)
    else:
        if n.right is None:
            n.right = BSNode(v)
        else:
            add_element(n.right,v)

head_node = BSNode(5)
add_element(head_node, 3)
add_element(head_node, 1)
add_element(head_node, 4)
add_element(head_node, 2)

assert head_node.content == 5
assert head_node.left.content == 3
assert head_node.left.left.content == 1
assert head_node.left.right.content == 4
assert head_node.left.left.right.content == 2

# 16.6 
# Given a binary search tree which contains integers as 
# values, calculate the sum of all the numbers.

def sum_bs(t):
    if t is None:
        return 0
    else:
        return t.content + sum_bs(t.left) + sum_bs(t.right)

head_node = BSNode(5)
add_element(head_node, 3)
add_element(head_node, 1)
add_element(head_node, 4)
add_element(head_node, 2)
assert sum_bs(head_node)==15

# 16.7 
# Insert a node into a sorted linked list (in order). 
# (Don’t forget about what happens when the new element is 
# at the start or end!)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        l = []
        current_idx = self.head
        while current_idx is not None:
            l.append(str(current_idx.value))
            current_idx = current_idx.next
        return ' -> '.join(l)
    def add_node(self, n):
        if self.head is None:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n

def sorted_insert(ll, n):
    current_idx = ll.head
    if n.value < current_idx.value:
        n.next = current_idx
        ll.head= n
    else:
        while current_idx.next is not None:
            if n.value < current_idx.next.value:
                break
            current_idx = current_idx.next
        n.next = current_idx.next
        current_idx.next = n

ll = LinkedList()
ll.add_node(Node(1))
ll.add_node(Node(3))
ll.add_node(Node(5))
ll.add_node(Node(7))
print(ll)
sorted_insert(ll,Node(2))
print(ll)
sorted_insert(ll,Node(0))
print(ll)
sorted_insert(ll,Node(999))
print(ll)

# 16.8 
# "Sort" a linked list that contains just 0s and 1s. That 
# is, modify the list such that all 0s come before all 1s.

def sort_ll(ll):
    zero_ll = LinkedList()
    one_ll = LinkedList()
    current_idx = ll.head
    while current_idx is not None:
        if current_idx.value == 0:
            zero_ll.add_node(current_idx)
        else:
            one_ll.add_node(current_idx)
        current_idx = current_idx.next
    if zero_ll.head is not None:
        ll.head = zero_ll.head
        zero_ll.tail.next = one_ll.head
    else:
        ll.head = one_ll.head
    if one_ll.head is not None:
        ll.tail = one_ll.tail
        one_ll.tail.next = None
    else:
        ll.tail = zero_ll.tail

ll = LinkedList()
ll.add_node(Node(0))
ll.add_node(Node(0))
sort_ll(ll)
assert ll.__str__() == '0 -> 0'

ll = LinkedList()
ll.add_node(Node(1))
ll.add_node(Node(1))
sort_ll(ll)
assert ll.__str__() == '1 -> 1'

ll = LinkedList()
ll.add_node(Node(1))
ll.add_node(Node(0))
ll.add_node(Node(1))
sort_ll(ll)
assert ll.__str__() == '0 -> 1 -> 1'

# 16.9 
# Write a function which takes a stack as input and returns 
# a new stack which has the elements reversed.

def flip_stack(s):
    n = list()
    s_copy = list(s)
    while s_copy:
        n.append(s_copy.pop())
    return n

s = [1, 2, 3]
assert flip_stack(s)==list(reversed(s))

# 16.10 
# Write a function which removes all the even numbers from 
# a stack. You should return the original stack, not a new 
# one.

def remove_evens(s):
    t = list()
    while s:
        v = s.pop()
        if v % 2 == 1:
            t.append(v)
    while t:
        s.append(t.pop())
    return s

assert remove_evens([1, 2, 3]) == [1, 3]
assert remove_evens([2, 4]) == []
assert remove_evens([1, 5, 7]) == [1, 5, 7]

# 16.11 
# Write a function to check if two queues are identical 
# (same values in the same order). It’s okay to 
# modify/destroy the two queues.

def check_identical(q1, q2):
    if len(q1) == len(q2):
        while q1 and q2:
            if q1.pop() != q2.pop():
                return False
        return True
    else:
        return False

assert check_identical([],[]) == True
assert check_identical([1, 2, 3],[1, 2, 3]) == True
assert check_identical([1, 3, 2],[1, 2, 3]) == False

# 16.12 
# Write a function to remove the 13th element from a queue 
# (but keep all the other elements in place and in the same 
# order).

def remove_13(q):
    if len(q) < 13:
        raise ValueError('too short')
    del q[12]
    return q

q = [11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114]
assert remove_13(q) == [11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 114]

# 16.13 
# Given two sorted arrays, write a function to merge them 
# in sorted order into a new array.

def merge(a1, a2):
    l = list()
    while a1 and a2:
        if a1[0] < a2[0]:
            l.append(a1.pop(0))
        else:
            l.append(a2.pop(0))
    while a1:
        l.append(a1.pop(0))
    while a2:
        l.append(a2.pop(0))
    return l

assert merge([1, 3, 5], [0, 4, 5]) == [0, 1, 3, 4, 5, 5]

# 16.14 
# Implement insertion sort.

def insertion_sort(l):
    for ii in range(1,len(l)):
        t = l[ii]
        jj = ii-1
        while jj >= 0 and t < l[jj]:
            l[jj+1] = l[jj]
            jj -= 1
        l[jj+1] = t
    return l

assert insertion_sort([99, 1, 0, 4, 3]) == sorted([99, 1, 0, 4, 3])
assert insertion_sort([]) == sorted([])
assert insertion_sort([1]) == sorted([1])
assert insertion_sort([1, 2]) == sorted([1, 2])

# 16.15 
# Implement binary search. That is, given a sorted array 
# of integers and a value, find the location of that value. 

def binary_search(l, v):
    first = 0
    last = len(l)-1
    while first <= last:
        mid = (last + first)//2
        if l[mid] == v:
            return mid
        elif l[mid] < v:
            first = mid+1
        else:
            last = mid-1
    raise ValueError('Not Found')

binary_search([],1)
assert binary_search([1,2,3],1)==0
assert binary_search([2,1,3],1)==1
assert binary_search([2,3,1],1)==2
binary_search([2,3,4],1)

# 16.16 
# You are given an integer array which was sorted, but then 
# rotated. It contains all distinct elements. Find the 
# minimum value. 
# For example, the array might be 
# 6, 8, 9, 11, 15, 20, 3, 4, 5. 
# The minimum value would obviously be 3.

def find_min(l):
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            return l[i]
    return l[0]

find_min([6, 8, 9, 11, 15, 20, 3, 4, 5])

# 16.17 
# Using depth-first search, check if a tree contains a value.

class TNode:
    def __init__(self, value):
        self.branches = []
        self.value = value

def dfs(t, v):
    if t.value == v:
        return True
    if t.branches:
        for b in t.branches:
            if dfs(b,v):
                return True
    return False

t = TNode(0)
t1 = TNode(1)
t2 = TNode(2)
t3 = TNode(3)
t21 = TNode(4)
t22 = TNode(5)
t.branches = [t1, t2, t3]
t2.branches = [t21, t22]
dfs(t, 6)

# 16.18 
# Write the pseudocode for breadth-first search on a binary 
# tree. Try to be as detailed as possible.

def bfs(t, v):
    b = [t]
    while b:
        current_node = b.pop(0)
        if current_node.value == v:
            return True
        b += current_node.branches
    return False

t = TNode(0)
t1 = TNode(1)
t2 = TNode(2)
t3 = TNode(3)
t21 = TNode(4)
t22 = TNode(5)
t.branches = [t1, t2, t3]
t2.branches = [t21, t22]
bfs(t, 6)

# 16.19 
# Design an algorithm and write code to find all solutions to 
# the equation a^3 + b^3 = c^3 + d^3 where a, b, c, and d are 
# positive integers less than 1000. If you wish, you can print 
# only “interesting” solutions. That is, you can ignore 
# solutions of the form x^3 + y^3 = x^3 + y^3 and solutions that 
# are simple permutations of other solutions (swapping left 
# and right hand sides, swapping a and b, swapping c and d). 
# For example, if you were printing all solutions less than 
# 20, you could choose to print only 23 + 163 = 93 + 153 and 
# 13 + 123 = 93 + 103.

def find_cube(lt = 1000):
    l = dict()
    r = list()
    for a in range(1, lt):
        for b in range(a, lt):
            cube_sum = a**3 + b**3
            if cube_sum in l:
                l[cube_sum].append((a, b))
                r.append(l[cube_sum])
            else:
                l[cube_sum] = [(a, b)]
    return r

# 16.20 
# Given a string, print all permutations of that string. You 
# can assume the word does not have any duplicate characters.

def print_perm(s):
    if len(s) == 1:
        return [s]
    else:
        l = []
        for i in range(len(s)):
            sub = s[:i] + s[i+1:]
            l += [s[i]+p for p in print_perm(sub)]
        return l

# 16.21 
# In a group of people, a person is called a “celebrity” if 
# everyone knows them but they know no one else. You are given 
# a function knows(a, b) which tells you if person a knows person 
# b. Design an algorithm to find the celebrity (if one exists). 
# For simplicity, you can assume that everyone is given a label 
# from 0 to N-1. You need to implement a function int 
# findCelebrity(int N). 
# Observe that: 
# (1) There can only be one celebrity at most (due to the 
# definition of a celebrity).
# (2) The knows function is the only way to look up who knows who.

def findCelebrity(people)
    p = list(people)
    candidate = p.pop()
    while p:
        contender = p.pop()
        if knows(candidate, contender):
            candidate = contender
    for norm in people:
        if knows(candidate, norm) or not knows(norm, candidate):
            return False
    return candidate

# 16.22 
# You have an NxN matrix of characters and a list of valid words 
# (provided in any format you wish). A word can be formed by starting 
# with any character and then moving up, down, left, or right. Words 
# do not have to be in a straight line (PACKING is a word below). You 
# cannot reuse a letter for the same word, so GOING (in the grid below) 
# would not be a word since it reuses the G. Design an algorithm and 
# write code to print all valid words. 
# L I G O 
# E P N I 
# N A C K 
# S M A R



# 16.23 
# Given an array of integers (with both positive and negative 
# values), find the contiguous sequence with the largest sum. 
# Return just the sum. 
# Example: 
# Input: 2, -8, 3, -2, 4, -10 
# Output: 5 (i.e., {3, -2, 4})

def find_largest_sum(l):
    max_value = 0
    running_sum = 0
    for i in range(len(l)):
        running_sum += l[i]
        if running_sum < 0:
            running_sum = 0
        elif running_sum > max_value:
            max_value = running_sum
    return max_value

assert find_largest_sum([2, -8, 3, -2, 4, -10])==5
find_largest_sum([])
find_largest_sum([10])
find_largest_sum([-10])

# Fibonacci

def fib1(n):
    if n < 2:
        return n
    else: 
        return fib(n-1) + fib(n-2)

def fib2(n):
    c = {0: 0, 1: 1}
    def fib_helper(n):
        if n not in c:
            c[n] = fib_helper(n-1) + fib_helper(n-2)
        return c[n]
    return fib_helper(n)

def fib3(n):
    c = {0: 0, 1: 1}
    for i in range(2, n+1):
        c[i] = c[i-1] + c[i-2]
    return c[n]
