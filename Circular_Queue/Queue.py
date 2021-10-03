########################################
# Circular Queue
# Author : Tom Choi
########################################

class CircularQueue:
    """
    Circular Queue Class
    """
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"
        result = ""
        str_list = [str(self.data[(self.head + i)%self.capacity]) for i in range(self.size)]
        return "Queue: " + (", ").join(str_list)

    def __len__(self):
        """
        returns the size of the queue
        :return: size
        """
        return self.size

    def is_empty(self):
        """
        check if the queue is empty
        :return: true if it is empty, otherwise false
        """
        return self.size == 0

    def head_element(self):
        """
        returns the front element of the Queue
        :return: front element
        """
        if self.is_empty():
            return None
        return self.data[self.head]

    def tail_element(self):
        """
        returns the back element of the queue
        :return: back element
        """
        if self.is_empty():
            return None
        return self.data[self.tail - 1]

    def enqueue(self, val):
        """
        add an element to the back of the queue
        :param val: value to add
        :return: none
        """
        if self.size == self.capacity - 1:
            self.tail = (self.tail + 1) % (self.capacity * 2)
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.data[self.tail - 1] = val
        self.size += 1
        if self.size == self.capacity:
            self.grow()

    def dequeue(self):
        """
        remove an element from the front
        :return: removed element
        """
        if self.is_empty():
            return None
        return_head = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.data[self.head - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity // 2 >= 4:
            self.shrink()
        return return_head

    def tail_dequeue(self):
        """
        remove an element from the back
        :return: removed element
        """
        if self.is_empty():
            return None
        return_tail = self.data[self.tail - 1]
        self.data[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity // 2 >= 4:
            self.shrink()
        return return_tail

    def grow(self):
        """
        doubles the capacity of the queue when size is equal to the capacity
        :return: none
        """
        v = [None] * (self.capacity * 2)
        head_count = self.head
        for i in range(self.size):
            v[i] = self.data[(head_count + i) % self.capacity]

        self.head = 0
        self.tail = self.size
        self.capacity *= 2
        self.data = v

    def shrink(self):
        """
        halves the capacity of the queue if the size is 1/4 or less but capacity should
        be bigger than 4
        :return: none
        """
        v = [None] * (self.capacity // 2)
        head_count = self.head
        for i in range(self.size):
            v[i] = self.data[(head_count + i) % self.capacity]

        self.head = 0
        self.tail = self.size
        self.capacity //= 2
        self.data = v

def greatest_val(w, values):
    """
    find the greatest value in the list values at each possible array of size w
    :param w: array size
    :param values:  list
    :return: the list of greatest values
    """
    if len(values) == 0:
        return []
    if w == 0:
        return []
    circ = CircularQueue()
    return_list = []

    biggest = values[0]
    for i in range(w):
        circ.enqueue(values[i])
        if biggest <= values[i]:
            biggest = values[i]
    return_list.append(biggest)
    i += 1
    count = i
    for j in range(len(values) - i):
        deq = circ.dequeue()
        circ.enqueue(values[j + w])
        biggest = values[count]
        for k in range(w):
            deq = circ.dequeue()
            if biggest <= deq:
                biggest = deq
            circ.enqueue(deq)
        return_list.append(biggest)
        count += 1
    return return_list
