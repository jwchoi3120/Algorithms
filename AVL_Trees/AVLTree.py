########################################
# AVL Tree
# Author : Tom Choi
########################################

import random as r      # To use for testing

class Node:
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None    # The root Node of the tree
        self.size = 0       # The number of Nodes in the tree

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    def visual(self):
        """
        Returns a visual representation of the AVL Tree in terms of levels
        :return: None
        """
        root = self.root
        if not root:
            print("Empty tree.")
            return
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = self.height(self.root)
        for i in range(h+1):
            track[i] = []
        while bfs_queue:
            node = bfs_queue.pop(0)
            track[node[1]].append(node)
            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
        for i in range(h+1):
            print(f"Level {i}: ", end='')
            for node in track[i]:
                print(tuple([node[0], node[2]]), end=' ')
            print()

    def insert(self, node, value):
        """
        takes in a value to be added in the form of a node to the tree
        :param node: node to add
        :param value: value of the node
        :return: none
        """
        if self.root is None:
            newNode = Node(value)
            self.root = newNode
            self.size += 1
            return
        else:
            if node.value == value:
                return
            if value < node.value:
                if node.left:
                    self.insert(node.left, value)
                else:
                    node.left = Node(value, parent=node)
                    self.size += 1
            elif value > node.value:
                if node.right:
                    self.insert(node.right, value)
                else:
                    node.right = Node(value, parent=node)
                    self.size += 1
        self.rebalance(node)

    def remove(self, node, value):
        """
        takes in a value to remove from the tree
        :param node: node to remove
        :param value: value of the node
        :return: root of the subtree
        """

        s_node = self.search(node, value)

        if s_node is None or s_node.value != value:
            return

        node = s_node
        parent = node.parent

        if self.size == 1 and self.root.value == value:
            self.root = None
            self.size -= 1
            return
        elif self.size == 2:
            if self.root.left and self.root.value == value:
                self.root.value = self.root.left.value
                self.root.left = None
                self.size -= 1
                return self.root
            if self.root.right and self.root.value == value:
                self.root.value = self.root.right.value
                self.root.right = None
                self.size -= 1
                return self.root
        if node.left is not None and node.right is not None:
            succNode = self.max(node.left)
            self.remove(self.root, succNode.value)
            s_node.value = succNode.value
            return self.root
        elif node == self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right
            if self.root:
                self.root.parent = None
            self.size -= 1
            return self.root
        elif node.left is not None:
            self.replace_child(parent, node, node.left)
            self.size -= 1
        else:
            self.replace_child(parent, node, node.right)
            self.size -= 1
        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent
        return node
    
    def search(self, node, value):
        """
        takes in a value to search for a node which is the
        root of a given tree or subtree
        :param node: node to found
        :param value: value of the node
        :return: node with the given value if found, else returns the
        potential parent node
        """
        cur = self.root
        while cur is not None:
            if value == cur.value:
                return cur
            elif value < cur.value:
                if cur.left is None:
                    return cur
                cur = cur.left
            else:
                if cur.right is None:
                    return cur
                cur = cur.right
        return None


    def inorder(self, node):
        """
        returns a generator object of the tree traversed using the
        inorder method of traversal starting at the given node
        :param node: given node
        :return: generator object
        """
        if node is None:
            return
        else:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)


    def preorder(self, node):
        """
        returns a generator object of the tree traversed using the
        preorder method of traversal starting at the given node
        :param node: given node
        :return: generator object
        """
        if node is None:
            return
        else:
            yield node
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)


    def postorder(self, node):
        """
        returns a generator object of the tree traversed using the
        postorder method of traversal starting at the given node
        :param node: given node
        :return: generator object
        """
        if node is None:
            return
        else:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node

    def depth(self, value):
        """
        depth of the node
        :param value: given value
        :return: depth
        """
        cur = self.root
        counter = 0
        while cur is not None:
            if value == cur.value:
                return counter
            elif value < cur.value:
                cur = cur.left
                counter += 1
            elif value > cur.value:
                cur = cur.right
                counter += 1
        return -1

    def height(self, node):
        """
        height of the tree
        :param node: given node
        :return: height
        """
        if not node:
            return -1
        return node.height


    def min(self, node):
        """
        minimum of the tree rooted at the given node
        :param node: given node
        :return: minimum value
        """
        if node is None or node.left is None:
            return node
        else:
            return self.min(node.left)

    def max(self, node):
        """
        maximum of the tree rooted at the given node
        :param node: given node
        :return: maximum value
        """
        if node is None or node.right is None:
            return node
        else:
            return self.max(node.right)


    def get_size(self):
        """
        get the size of the tree
        :return: number of nodes in the AVL tree
        """
        return self.size


    def get_balance(self, node):
        """
        returns the balance factor of the node passed in
        :param node: given node
        :return: leftheight - rightheight
        """
        leftHeight = -1
        if node.left is not None:
            leftHeight = node.left.height
        rightHeight = -1
        if node.right is not None:
            rightHeight = node.right.height
        return leftHeight - rightHeight

    def left_rotate(self, root):
        """
        rotate left
        :param root: root of the subtree
        :return: none
        """
        rightLeftChild = root.right.left
        if root.parent is not None:
            self.replace_child(root.parent, root, root.right)
        else:
            self.root = root.right
            self.root.parent = None
        self.set_child(root.right, "left", root)
        self.set_child(root, "right", rightLeftChild)
        self.update_height(root)

    def right_rotate(self, root):
        """
        rotate right
        :param root: root of the subtree
        :return: none
        """
        leftRightChild = root.left.right
        if root.parent is not None:
            self.replace_child(root.parent, root, root.left)
        else:
            self.root = root.left
            self.root.parent = None
        self.set_child(root.left, "right", root)
        self.set_child(root, "left", leftRightChild)
        self.update_height(root)

    def update_height(self, node):
        """
        update the height
        :param node: given node
        :return: none
        """
        leftHeight = -1
        if node is not None:
            if node.left is not None:
                leftHeight = node.left.height
            rightHeight = -1
            if node.right is not None:
                rightHeight = node.right.height
            if leftHeight > rightHeight:
                node.height = leftHeight + 1
            elif leftHeight <= rightHeight:
                node.height = rightHeight + 1

    def set_child(self, parent, whichChild, child):
        """
        sets the child of subtree
        :param parent: parent node
        :param whichChild: select left or right
        :param child: child node
        :return: none
        """
        if whichChild != "left" and whichChild != "right":
            return False
        if whichChild == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        self.update_height(child)
        return True

    def replace_child(self, parent, currentChild, newChild):
        """
        replaces child in the subtree
        :param parent: parent node
        :param currentChild: current node
        :param newChild: changing into new node
        :return: setchild
        """
        if parent.left == currentChild:
            return self.set_child(parent, "left", newChild)
        elif parent.right == currentChild:
            return self.set_child(parent, "right", newChild)
        return False

    def rebalance(self, node):
        """
        rebalances the subtree rooted at node, if needed
        :param node: given node
        :return: root of the new, balanced subtree
        """
        self.update_height(node)
        if self.get_balance(node) == -2:
            if self.get_balance(node.right) == 1:
                self.right_rotate(node.right)
            return self.left_rotate(node)
        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                self.left_rotate(node.left)
            return self.right_rotate(node)
        return node


def repair_tree(tree):
    """
    takes in a tree where two values may have been swapped,
    violating the BST property of nodes on the right being larger
    than the parent node
    :param tree: AVL tree
    :return: none
    """

    if tree.root is None:
        return
    if tree.root.left is None and tree.root.right is None:
        return
    l = []
    gen = tree.inorder(tree.root)
    for k in range(tree.size):
        l.append(next(gen, None).value)
    val = l[0]
    swap1 = 0
    swap2 = 0
    for i in range(1, tree.size):
        if val < l[i]:
            val = l[i]
        elif val > l[i]:
            swap1 = l[i-1]
            val = l[i]
            break
    val1 = l[-1]
    for ele in reversed(l):
        if val1 == ele:
            val1 = ele
            continue
        elif val1 > ele:
            val1 = ele
        elif val1 < ele:
            swap2 = val1
            break
    swap(tree.root, swap1, swap2)

def swap(node, swap1, swap2):
    """
    swap two nodes
    """
    if node is None:
        return
    if node.value == swap1:
        node.value = swap2
    elif node.value == swap2:
        node.value = swap1
    swap(node.left, swap1, swap2)
    swap(node.right, swap1, swap2)
