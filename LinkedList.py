########################################
# Linked List
# Author : Tom Choi
########################################


class Node:
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


class LinkedList:
    def __init__(self):
        """
        Create/initialize an empty linked list
        """
        self.head = None  # Node
        self.tail = None  # Node
        self.size = 0  # Integer

    def __eq__(self, other):
        """
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    __str__ = __repr__

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        get the length of linked list
        :return: returns size
        """
        return self.size

    def is_empty(self):
        """
        check if linked list is empty
        :return: returns true if size is zero, false if not
        """
        if self.size == 0:
            return True
        return False

    def front_value(self):
        """
        get the front value of the linked list
        :return: None if size is zero, if not, return value of head
        """
        if self.size == 0:
            return None
        return self.head.value

    def back_value(self):
        """
        get the back value of the linked list
        :return: None if size is zero, if not, return value of tail
        """
        if self.size == 0:
            return None
        return self.tail.value

    def count(self, val):
        """
        count how many same values there are
        :param val: value that put in to see how many same values there are
        :return: the number of how many same values there are
        """
        temp = 0
        node = self.head
        while node:
            if node.value == val:
                temp += 1
            node = node.next_node
        return temp

    def find(self, val):
        """
        find the same value as input
        :param val: value to find if the value is in the linked list
        :return: True if found, false if not
        """
        temp = self.count(val)
        if temp >= 1:
            return True
        else:
            return False

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        add the value into front of linked list
        :param val: value to put at the front of linked list
        :return: nothing
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head = node
        self.size += 1

    def push_back(self, val):
        """
        add the value into back of linked list
        :param val: value to put at the back of linked list
        :return: nothing
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        """
        take out the value fron front of linked list
        :return: the value that you popped at the front
        """
        if self.size == 0:
            return None
        pop = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return pop

    def pop_back(self):
        """
        take out the value from back of linked list
        :return: the value that you popped at the back
        """
        if self.size == 0:
            return None
        pop = self.tail.value
        if not self.head.next_node:
            self.head = self.tail = None

        node = self.head
        while node:
            if node.next_node == self.tail:
                node.next_node = None
                self.tail = node
            node = node.next_node
        self.size -= 1
        return pop


def partition(linked_list, x):
    """
    partition the linked list with input value
    :param linked_list: the linked list that you are going to partition
    :param x: the value of the input
    :return: the new linked list that is changed after partition
    """

    lower_num_link = LinkedList()
    bigger_num_link = LinkedList()
    
    for i in range(linked_list.length()):
        lower_num_link.push_back(linked_list.front_value())
        bigger_num_link.push_back(linked_list.front_value())
        linked_list.pop_front()
        
    newLink = LinkedList()
    
    for i in range(lower_num_link.length()):
        if lower_num_link.front_value() < x:
            newLink.push_back(lower_num_link.front_value())
            lower_num_link.pop_front()
        else:
            lower_num_link.pop_front()
            continue

    for i in range(bigger_num_link.length()):
        if bigger_num_link.front_value() >= x:
            newLink.push_back(bigger_num_link.front_value())
            bigger_num_link.pop_front()
        else:
            bigger_num_link.pop_front()
            continue
            
    return newLink

def main():
    """
    testing if everything works fine.
    1. push_back
    2. push_front
    3. length
    4. is_empty
    5. front_value
    6. back_value
    7. find
    8. pop_front
    9. pop_back
    10. partition
    """
    
    #1. push_back
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    assert str(llist) == "[1, 2, 3, 4]"
    
    #2 push_front
    llist = LinkedList()
    llist.push_front(1)
    llist.push_front(2)
    llist.push_front(3)
    llist.push_front(4)
    assert str(llist) == "[4, 3, 2, 1]"

    #3 length
    llist = LinkedList()
    llist.push_front(1)
    llist.push_front(2)
    llist.push_front(3)
    llist.push_front(4)
    assert llist.length() == 4

    #4 is_empty
    llist = LinkedList()
    assert llist.is_empty()
    llist.push_front(1)
    llist.push_front(2)
    llist.push_front(3)
    llist.push_front(4)
    assert not llist.is_empty()

    #5 front_value
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    assert llist.front_value() == 1

    #6 back_value
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    assert llist.back_value() == 4

    #7 find
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    assert llist.find(2)
    assert not llist.find(5)

    #8 pop_front
    llist = LinkedList()
    llist.push_front(1)
    llist.push_front(2)
    llist.push_front(3)
    llist.push_front(4)
    assert llist.pop_front() == 4
    assert str(llist) == "[3, 2, 1]"

    #9 pop_back
    llist = LinkedList()
    llist.push_front(1)
    llist.push_front(2)
    llist.push_front(3)
    llist.push_front(4)
    assert llist.pop_back() == 1
    assert str(llist) == "[4, 3, 2]"

    #10 partition
    llist = LinkedList()
    llist.push_back(5)
    llist.push_back(4)
    llist.push_back(2)
    llist.push_back(1)
    llist = partition(llist, 3)
    assert str(llist) == "[2, 1, 5, 4]"
    llist2 = LinkedList()
    llist2.push_back(5)
    llist2.push_back(4)
    llist2.push_back(2)
    llist2.push_back(1)
    llist2 = partition(llist2, 7)
    assert str(llist2) == "[5, 4, 2, 1]"
    llist3 = LinkedList()
    llist3.push_back(5)
    llist3.push_back(4)
    llist3.push_back(2)
    llist3.push_back(1)
    llist3 = partition(llist3, 2)
    assert str(llist3) == "[1, 5, 4, 2]"
    
    print("Linked List Functions All Passed!")
    
main()