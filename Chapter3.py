# 3.1
# Describe how you could use a single array to implement three stacks.

class SingleArrayStacks:
    def __init__(self, n = 100, stacks = 3):
        self.stack_size = n
        self.stack_cnt = stacks
        self.array = [None] * self.stack_cnt * self.stack_size
        self.pointer = [-1] * self.stack_cnt
    def push(self, stacknum, value):
        if self.pointer[stacknum] + 1 < self.stack_size:
            self.pointer[stacknum] += 1
            self.array[stacknum * self.stack_size + self.pointer[stacknum]] = value
        else:
            print('Out of space')
    def pop(self, stacknum):
        if self.pointer[stacknum] > -1:
            self.pointer[stacknum] -= 1
            return self.array[stacknum * self.stack_size + self.pointer[stacknum] + 1]
        else:
            print('Stack empty')
    def peak(self, stacknum):
        if self.pointer[stacknum] > -1:
            return self.array[stacknum * self.stack_size + self.pointer[stacknum] + 1]
        else:
            print('Stack empty')

array = SingleArrayStacks()
array.push(2,1)
array.push(2,2)
array.push(2,3)
array.peak(0)
array.pop(2)
array.pop(2)
array.pop(2)
array.pop(2)

# 3.2
# How would you design a stack which, in addition to push and pop, also has a function 
# min which returns the minimum element? Push, pop and min should all operate in O(1) time

class StackWithMin():
    def __init__(self):
        self.value_stack = list()
        self.min_stack = list()
    def push(self, value):
        self.value_stack.append(value)
        if len(self.min_stack) > 0:
            self.min_stack.append(min(self.min_stack[-1], value))
        else:
            self.min_stack.append(value)
    def pop(self):
        return (self.value_stack.pop(), self.min_stack.pop())
    def peak(self):
        return (self.value_stack[-1], self.min_stack[-1])

stack = StackWithMin()
stack.push(0)
stack.push(10)
stack.push(-999)
stack.peak()
stack.pop()
stack.pop()
stack.pop()

# 3.3
# Imagine a (literal) stack of plates If the stack gets too high, it might topple. Therefore,
# in real life, we would likely start a new stack when the previous stack exceeds 
# some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks
# should be composed of several stacks, and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should 
# behave identically to a single stack (that is, pop() should return the same values as it
# would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific
# sub-stack.

class SetOfStacks():
    def __init__(self, capacity = 3):
        self.capacity = capacity
        self.stack_array = [list()]
    def push(self, value):
        if len(self.stack_array[-1]) >= self.capacity:
            self.stack_array.append(list())
        self.stack_array[-1].append(value)
    def pop(self):
        if not self.stack_array[-1]:
            self.stack_array.pop()
        return self.stack_array[-1].pop()
    def popAt(self, idx):
        return self.stack_array[idx].pop()

sos = SetOfStacks()
sos.push(1)
sos.push(2)
sos.push(3)
sos.push(4)
sos.push(5)
sos.pop()
sos.pop()
sos.pop()
sos.pop()
sos.pop()

# 3.4
# In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different
# sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending
# order of size from top to bottom (e.g., each disk sits on top of an even larger one). You
# have the following constraints:
# (A) Only one disk can be moved at a time.
# (B) A disk is slid off the top of one rod onto the next rod.
# (C) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first rod to the last using Stacks.

class Hanoi:
    def __init__(self,n = 5):
        self.num_disks = n
        self.rods = [list(reversed(list(range(self.num_disks)))), list(), list()]
    def __str__(self):
        return str(self.rods)
    def move_disk(self, from_rod, to_rod):
        self.rods[to_rod].append(self.rods[from_rod].pop())
    def move_n(self, n, from_rod, to_rod, int_rod):
        if n>1:
            self.move_n(n-1, from_rod, int_rod, to_rod)
            self.move_disk(from_rod, to_rod)
            self.move_n(n-1, int_rod, to_rod, from_rod)
        else:
            self.move_disk(from_rod, to_rod)
    def play(self):
        self.move_n(self.num_disks, 0, 2, 1)

h = Hanoi()
print(h)
h.play()
print(h)

# 3.5
# Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self):
        self.list1 = list()
        self.list2 = list()
    def _transfer(self, from_stack, to_stack):
        for _ in range(len(from_stack)):
            to_stack.append(from_stack.pop())
    def push(self, value):
        self.list1.append(value)
    def pop(self):
        if len(self.list2) == 0:
            self._transfer(self.list1, self.list2)
        return self.list2.pop()
    def peak(self):
        if len(self.list2) == 0:
            self._transfer(self.list1, self.list2)
        return self.list2[-1]

mq = MyQueue()
mq.push(1)
mq.push(2)
mq.push(3)
mq.peak()
mq.pop()
mq.pop()
mq.push(99)
mq.pop()
mq.pop()

# 3.6 Write a program to sort a stack in ascending order You should not make any assumptions 
# about how the stack is implemented. The following are the only functions that 
# should be used to write this program: push | pop | peek | isEmpty

def sort_stacks(from_stack):
    to_stack = list()
    temp_stack = list()
    while len(from_stack) > 0:
        while len(to_stack) > 0 and from_stack[-1] < to_stack[-1]:
            temp_stack.append(to_stack.pop())
        to_stack.append(from_stack.pop())
        while len(temp_stack) > 0:
            to_stack.append(temp_stack.pop())
    return to_stack

import random
sort_stacks([random.randint(0,9) for _ in range(10)])
