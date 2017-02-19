# 1.1 
# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?

def all_unique(s1):
    return len(s1) == len(set(s1))

def all_unique_no_structs(s1):
    for c in s1:
        if s1.count(c) > 1:
            return False
    return True

# 1.2
# Write code to reverse a C-Style String 

def rev_str(s1):
    return s1[::-1]

# 1.3 
# Design an algorithm and write code to remove the duplicate characters in a string 
# without using any additional buffer NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.

def remove_dup(s1):
    l = list(s1)
    last_char = s1[0]
    for i in range(1,len(l)):
        if l[i] == last_char:
            l[i] = ''
        else:
            last_char = l[i]
    return ''.join(l)

def remove_dup_no_buf(s1):
    return ''.join([s1[i] for i in range(len(s1)-1) if s1[i] is not s1[i+1]] + [s1[-1]])

# 1.4 
# Write a method to decide if two strings are anagrams or not.

import collections
def is_anagram(s1, s2):
    if len(s1) == len(s2):
        return collections.Counter(s1) == collections.Counter(s2)
    return False

# 1.5
# Write a method to replace all spaces in a string with '%20'.

def replace_space(s1):
    return s1.replace(' ','%20')

# 1.6
# Given an image represented by an NxN matrix, where each pixel in the image is 4 
# bytes, write a method to rotate the image by 90 degrees Can you do this in place?

def rotate_mat(m):
    n = len(m)
    return [[r[i] for r in reversed(m)] for i in range(n)]

# Test case

mat = [[1,2,3],[4,5,6],[0,8,9]]

# 1.7
#  Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
# column is set to 0.

def zero_mat(mat):
    m = len(mat)
    n = len(mat[0])
    zero_row = set()
    zero_col = set()
    for m_i in range(m):
        for n_i in range(n):
            if mat[m_i][n_i] == 0:
                zero_row.add(m_i)
                zero_col.add(n_i)
    new_mat = list()
    for m_i in range(m):
        if m_i in zero_row:
            new_mat.append([0] * n)
        else:
            new_mat.append([0 if (i in zero_col) else mat[m_i][i] for i in range(n)])
    return new_mat

# 1.8
# Assume you have a method isSubstring which checks if one word is a substring of 
# another Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using 
# only one call to isSubstring (i e , “waterbottle” is a rotation of “erbottlewat”)

def isSubstring(s1, s2):
    return s1.find(s2) > -1

def sub_check(s1, s2):
    if len(s1) == len(s2):
        return isSubstring(s1 * 2, s2)
    return False
