########################################
# Recursion
# Author : Tom Choi
########################################


class LinkedNode:
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __repr__(self):
        """
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


def insert(value, node=None):
    """
    inserts value into the linked node
    :param value: value of it
    :param node: node has value into it
    :return: node which is head
    """
    if node is None:
        node = LinkedNode(value)

    elif node.next_node is None:
        new_node = LinkedNode(value)
        node.next_node = new_node
    else:
        insert(value, node.next_node)

    return node


def string(node):
    """
    print linked node as a string
    :param node: head node
    :return: string nodes
    """
    if not node:
        return None
    elif node != None and node.next_node != None:
        return str(node) + ", " + string(node.next_node)
    elif node != None:
        return str(node.value)


def remove(value, node):
    """
    remove the node that has specific value
    :param value: value to delete
    :param node: head node
    :return: head of the list
    """
    if not node:
        return None
    elif value == node.value:
        return node.next_node
    else:
        node.next_node = remove(value, node.next_node)
    return node


def remove_all(value, node):
    """
    remove all the nodes that has same value as input value
    :param value: input value
    :param node: head node
    :return: head node
    """
    if not node:
        return None
    if node.value == value:
        return remove_all(value, node.next_node)
    node.next_node = remove_all(value, node.next_node)
    return node


def search(value, node):
    """
    search the node that has same value
    :param value: value to search
    :param node: head node
    :return: the searched node
    """
    if not node:
        return False
    elif value == node.value:
        return True
    return search(value, node.next_node)


def length(node):
    """
    length of the linked node
    :param node: head node
    :return: length of the linked node
    """
    if not node:
        return 0
    else:
        return 1 + length(node.next_node)


def sum_all(node):
    """
    add all the values in the linked node
    :param node:
    :return: added value
    """
    if not node:
        return 0
    else:
        return node.value + sum_all(node.next_node)


def count(value, node):
    """
    count how many nodes have same value as input value
    :param value: input value
    :param node: head node
    :return: number of how many nodes have same value as input value
    """
    if not node:
        return 0
    elif value != node.value:
        return count(value, node.next_node)
    else:
        return 1 + count(value, node.next_node)


# Application Problem
def palindrome(node, length, nodes):
    """
    check if the linked node is a palindrome
    :param node: input node head
    :param length: length of the linked node
    :param nodes: empty list
    :return: true if it is a palindrome false if not
    """
    if nodes[0] is None or not nodes:
        if nodes:
            nodes[0] = node
        else:
            nodes.append(node)

    if node is None:
        return True
    if not palindrome(node.next_node, length - 2, nodes):
        return False

    if node.value != nodes[0].value:
        return False
    else:
        nodes[0] = nodes[0].next_node
        return True


def main():
    """
    testing if everything works fine.
    1. insert
    2. string
    3. length
    4. search
    5. count
    6. sum_all
    7. remove
    8. remove_all
    9. palindrome
    """
    
    #1 insert
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    for i in range(1, 5):
    	assert llist.value == i
    	llist = llist.next_node

    #2 string
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    assert string(llist) == "1, 2, 3, 4"

    #3 length
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    assert length(llist) == 4

    #4 search
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    assert search(2, llist)

    #5 count
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    insert(1, llist)
    assert count(1, llist) == 2

    #6 sum_all
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    assert sum_all(llist) == 10

    #7 remove
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    llist = remove(2, llist)
    for i in [1, 3, 4]:
        assert llist.value == i
        llist = llist.next_node

    #8 remove_all
    llist = insert(1)
    insert(2, llist)
    insert(3, llist)
    insert(4, llist)
    insert(1, llist)
    llist = remove_all(1, llist)
    for i in range(2, 5):
        assert llist.value == i
        llist = llist.next_node

    #9 palindrome
    llist = insert('a')
    insert('b', llist)
    insert('c', llist)
    insert('b', llist)
    insert('a', llist)
    assert palindrome(llist, length(llist), [None]) == True
    
    llist2 = insert('f')
    insert('a', llist2)
    insert('l', llist2)
    insert('s', llist2)
    insert('e', llist2)
    assert palindrome(llist2, length(llist2), [None]) == False

    print("Recursion Functions All Passed!")

main()
