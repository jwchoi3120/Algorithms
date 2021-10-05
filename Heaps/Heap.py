########################################
# Heaps
# Author : Tom Choi
########################################

class Node:
    __slots__ = ('_key', '_val')

    def __init__(self, key, val):
        self._key = key
        self._val = val

    def __lt__(self, other):
        return self._key < other._key or (self._key == other._key and self._val < other._val)

    def __gt__(self, other):
        return self._key > other._key or (self._key == other._key and self._val > other._val)

    def __eq__(self, other):
        return self._key == other._key and self._val == other._val

    def __str__(self):
        return '(k: {0} v: {1})'.format(self._key, self._val)

    __repr__ = __str__

    @property
    def val(self):
        """
        :return: underlying value of node
        """
        return self._val


class Heap:
    __slots__ = ('_size', '_capacity', '_data')

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity + 1  # additional element space for push
        self._data = [None for _ in range(self._capacity)]

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)

    __repr__ = __str__

    def __len__(self):  # allows for use of len(my_heap_object)
        return self._size

    def _parent(self, j):
        """
        get the parent index
        :param j: nodeindex
        :return: index
        """
        return (j - 1) // 2

    def _left(self, j):
        """
        get the left child's index
        :param j: nodeindex
        :return: index
        """
        return 2 * j + 1

    def _right(self, j):
        """
        get the right child's index
        :param j: nodeindex
        :return: index
        """
        return 2 * j + 2

    def _has_left(self, j):
        """
        check if the node has left
        :param j: nodeindex
        :return: bool
        """
        return self._left(j) < self._size  # index beyond end of list?

    def _has_right(self, j):
        """
        check if the node has right
        :param j: nodeindex
        :return: bool
        """
        return self._right(j) < self._size  # index beyond end of list?

    def _swap(self, i, j):
        """
        swap two nodes
        :param i: first index
        :param j: second index
        :return: none
        """
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def check_power_of_two(self, a):
        """
        check if a is power of two
        :param a: number
        :return: bool
        """
        if (a & (a - 1)):
            return False
        else:
            return True

    def _percolate_up(self):
        """
        when an element initially exists in the last spot of the underlying data list, percolate it up
        :return: none
        """
        nodeindex = self._size - 1
        parentindex = self._parent(nodeindex)
        while nodeindex > 0:
            if self._data[nodeindex] > self._data[parentindex]:
                return
            else:
                self._swap(nodeindex, parentindex)
                nodeindex = parentindex
                parentindex = self._parent(parentindex)

    def _percolate_down(self):
        """
        when an element innitially exists in the first spot of the underlying data list, percolate it down
        :return: none
        """
        j = 0
        check = True
        while check:
            check = False
            if self._has_left(j):
                left = self._left(j)
                small_child = left  # although right may be smaller
                if self._has_right(j):
                    right = self._right(j)
                    if self._data[right] < self._data[left]:
                        small_child = right

                if self._data[small_child] < self._data[j]:
                    self._swap(j, small_child)
                    j = small_child
                    check = True

    def _min_child(self, i):
        """
        given an index of a node, return the index of the smaller child
        :param i: node index
        :return: smaller child
        """
        if self.empty:
            return -1
        if self._has_left(i) is False and self._has_right(i) is False:
            return -1
        if self._has_left(i) and self._has_right(i) is False:
            return self._left(i)
        if self._has_left(i) and self._has_right(i):
            if self._left(i) > self._right(i):
                return self._right(i)
            else:
                return self._left(i)

    def push(self, key, val):
        """
        push the node into the heap
        :param key:
        :param val:
        :return:
        """
        self._data[self._size] = Node(key, val)
        self._size += 1
        self._percolate_up()

        if self._size >= self._capacity:
            self.pop()

        return None

    def pop(self):
        """
        pop the root of the heap
        :return: root
        """
        if self.empty:
            return None
        returnValue = self.top
        self._swap(0, self._size - 1)
        self._data[self._size - 1] = None
        self._size -= 1
        self._percolate_down()
        return returnValue

    @property
    def empty(self):
        """
        check if the heap is empty
        :return: bool
        """
        return self._size == 0

    @property
    def top(self):
        """
        return the root
        :return: root's value
        """
        if self.empty:
            return None
        return self._data[0]._val

    @property
    def levels(self):
        """
        returns all node values on a single level into a list
        :return: list
        """
        if self.empty:
            return []
        returnList = []
        l = []
        size = 0
        temp = 0
        l.append(self._data[0])
        returnList.append(l)
        l = []
        count = 1
        while count < self._size:
            if count == 2:
                l.append(self._data[count])
                returnList.append(l)
                l = []
                size = 0
            elif self.check_power_of_two(size + 1) and 2 < size and temp < size:
                l.append(self._data[count])
                returnList.append(l)
                l = []
                temp = size
                size = 0
            else:
                l.append(self._data[count])
                size += 1
            count += 1

        if size is not 0:
            returnList.append(l)
        return returnList

def most_x_common(vals, X):
    """
    return the X most commonly occuring elements
    :param vals: lists of strings
    :param X: how many common elements
    :return: set of those strings
    """
    dict = {}
    heap = Heap(X)
    returnSet = set()
    for item in vals:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    for item in dict:
        val = dict.get(item)
        heap.push(val, item)
    for i in range(X):
        returnSet.add(heap.pop())
    return returnSet









