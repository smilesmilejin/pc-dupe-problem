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

## Notes for the Interviewer

### Clarifying Questions

#### Q: Should I modify the list that was passed in or create a new list?

A: You can do either.

#### Q: What should I do if the input is None?

A: You can assume the input will include at least two nodes and the expected output will include at least one node.

#### Q: What should I do if the list has only a single element?

A: You can assume the input will include at least two nodes and the expected output will include at least one node.

#### Q: Will the input contain any cycles?

A: No.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: What data types will be stored in the values?

A: Integers, but more generally, if we assume that all the values in the list are mutually comparable, would the type matter?

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If your candidate still struggles to form an algorithm, ask them what data structure might be most useful for checking if a value has been seen before.

- It can be challenging to debug this problem. If your candidate is failing a test and unsure why, encourage them to add print statements that help them see values are in the list that is being returned from their function.

- It is OK for your candidate to use other intermediate data structures as part of their solution, but remind them that their final output MUST be a linked list using the provided Node class.

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What are the time/space complexities of each sample solution?
- How does the `__eq__` function on the Node class work?
- What is the time/space complexity of the `__eq__` function on the Node class?
- How could the `__eq__` method be improved to more robustly handle cycle detection and avoid `RecursionError`s?
