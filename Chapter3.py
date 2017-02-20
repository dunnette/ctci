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

# 3.4
# In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different
# sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending
# order of size from top to bottom (e.g., each disk sits on top of an even larger one). You
# have the following constraints:
# (A) Only one disk can be moved at a time.
# (B) A disk is slid off the top of one rod onto the next rod.
# (C) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first rod to the last using Stacks.

n = 5
rod1 = list(range(n))
rod2 = list()
rod3 = list()

# 3.5
# Implement a MyQueue class which implements a queue using two stacks.

# 3.6 Write a program to sort a stack in ascending order You should not make any assumptions 
# about how the stack is implemented. The following are the only functions that 
# should be used to write this program: push | pop | peek | isEmpty

