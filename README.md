# Dupe Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

Write a function that takes a _sorted_ singly linked list and returns a _sorted_ linked list that has the duplicates from the original removed.

For example, if we have a linked list with the following elements:

3 → 7 → 7 → 9 → 9 → 22

after removing duplicates, we would get the following output list:

3 → 7 → 9 → 22

In this example, the duplicates for 7 and 9 are removed. Note that the output is still in sorted order.

The input list will be represented using the provided `Node` class. The output **MUST ALSO** be a linked list using the provided `Node` class.

It is guaranteed that the list will not have any cycles.

Adapted from: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## Examples

### Example 1

Removing duplicates from the following list

1 → 2 → 2 → 3

produces

1 → 2 → 3

### Example 2

Removing duplicates from the following list

4 → 5 → 6

produces

4 → 5 → 6

### Example 3

Removing duplicates from the following list

3 → 7 → 7 → 9 → 9 → 22

produces

3 → 7 → 9 → 22

### Example 4

Removing duplicates from the following list

2 → 5 → 5 → 5 → 8

produces

2 → 5 → 8

### Example 5

Removing duplicates from the following list

8 → 8 → 8 → 8

produces

8
