# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")


# IMPLEMENTATION OPTION 1: Use a seen set
def remove_duplicates(head):
    seen = {head.value}  # Create a set tracking which values we've seen before
    new_head = Node(head.value)  # Create a new node with the same value as the input head
    new_current = new_head
    old_current = head.next

    while old_current:  # iterate through the input list
        value = old_current.value
        if value not in seen:  # if we haven't seen this value before
            seen.add(value)  # mark it as seen
            new_current.next = Node(value)  # create a new node with the value on the tail
            new_current = new_current.next  # move to the tail of our new list
        old_current = old_current.next  # move to the next element of the input list

    return new_head

    
# IMPLEMENTATION OPTION 2: Modify in-place (relies on assumption that input is sorted)
def remove_duplicates_alternative(head):
    current = head  # current keeps track of the node we're currently visiting

    while current is not None and current.next is not None:  # iterate through each node
        if current.value == current.next.value:  # if the next node is a duplicate
            current.next = current.next.next  # skip it
        else:  # if the next node is not a duplicate
            current = current.next  # move to that node

    return head


# Input: 1->2->2->3
# Expected output: 1->2->3
list_1 = Node(1, Node(2, Node(2, Node(3))))
expected_1 = Node(1, Node(2, Node(3)))
assert remove_duplicates(list_1) == expected_1

# Input: 4->5->6
# Expected output: 4->5->6
list_2 = Node(4, Node(5, Node(6)))
expected_2 = Node(4, Node(5, Node(6)))
assert remove_duplicates(list_2) == expected_2

# Input: 3->7->7->9->9->22
# Expected output: 3->7->9->22
list_3 = Node(3, Node(7, Node(7, Node(9, Node(9, Node(22))))))
expected_3 = Node(3, Node(7, Node(9, Node(22))))
assert remove_duplicates(list_3) == expected_3

# Input: 2->5->5->5->8
# Expected output: 2->5->8
list_4 = Node(2, Node(5, Node(5, Node(5, Node(8)))))
expected_4 = Node(2, Node(5, Node(8)))
assert remove_duplicates(list_4) == expected_4

# Input: 8->8->8->8
# Expected output: 8
list_5 = Node(8, Node(8, Node(8, Node(8, Node(8)))))
expected_5 = Node(8)
assert remove_duplicates(list_5) == expected_5

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
