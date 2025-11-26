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


def remove_duplicates(head):
    # Your solution here!
    pass

    # if LL has length of 1
        # return head


    # set a new_head point to head
    # new_head.next = None
    # pointer_node = new_head

    # if new_head.next 

    # current = new_head.next
    # loop throught the SSL, start with the second node 
        # if current.value != point_node:
            # point_node.next = current
            # point_node.next.next = None

        # current = current.next

    # return new_head

    # if not head.next:
    #     return head
    
    # new_head = head
    # new_head.next = None
    # point_node = new_head

    # current = new_head.next

    # while current:
    #     if current.value != point_node.value:
    #         point_node.next = current
    #         point_node.next.next = None

    #     current = current.next

    # # print('####### result SSL')
    
    # # cur = new_head

    # # while cur:
    # #     print(cur.value)
    # #     cur = cur.next

    # return new_head


    if not head.next:
        return head
    

    point_node = head
    current = head.next

    while current:
        if current.value == point_node.value:
            # print(f'current value {current.value} is equal to point value {point_node.value}')
            point_node.next = None

        elif current.value != point_node.value:
            point_node.next = current
            point_node = current

        current = current.next

        # print('####### result SSL')

        # cur = head

        # while cur:
        #     print(cur.value)
        #     cur = cur.next

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
