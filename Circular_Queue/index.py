from Circular_Queue.Queue import CircularQueue, greatest_val

def main():
    """
    testing if everything works fine.
    1. accessors
    2. enqueue
    3. dequeue
    4. tail_dequeue
    5. grow
    6. shrink
    7. greatest_val
    """

    #1 accessors
    queue = CircularQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.is_empty() == False 
    assert len(queue) == 4 
    assert queue.head_element() == 1
    assert queue.tail_element() == 4

    #2 enqueue
    queue = CircularQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.data == [10,20,30,None]
    assert queue.size == 3
    assert queue.head == 0
    assert queue.tail == 3
    assert queue.capacity == 4

    #3 dequeue
    queue = CircularQueue(6)
    for i in range(0,5):
        queue.enqueue(i*5)

    assert queue.data == [0,5,10,15,20,None]
    assert queue.size == 5
    assert queue.capacity == 6
    assert queue.head == 0
    assert queue.tail == 5
    queue.dequeue()
    assert queue.data == [None,5,10,15,20,None]
    assert queue.size == 4
    assert queue.capacity == 6
    assert queue.head == 1
    assert queue.tail == 5

    #4 tail_dequeue
    queue = CircularQueue(6)
    for i in range(0,5):
        queue.enqueue(i*5)

    assert queue.data == [0,5,10,15,20,None]
    assert queue.size == 5
    assert queue.capacity == 6
    assert queue.head == 0
    assert queue.tail == 5
    queue.tail_dequeue()
    assert queue.data == [0,5,10,15,None,None]
    assert queue.size == 4
    assert queue.capacity == 6
    assert queue.head == 0
    assert queue.tail == 4

    #5 grow
    queue= CircularQueue(5)
    for i in range(0,8):
        queue.enqueue(i*2)

    assert queue.data == [0,2,4,6,8,10,12,14,None,None]
    assert queue.capacity == 10
    assert queue.size == 8
    assert queue.head == 0
    assert queue.tail == 8

    #6 shrink
    queue = CircularQueue()
    for i in range(0,5):
        queue.enqueue(i)

    assert queue.data == [0,1,2,3,4,None,None,None]
    assert queue.size == 5
    assert queue.capacity == 8
    assert queue.head == 0
    assert queue.tail == 5
    for i in range(3):
        queue.tail_dequeue()

    assert queue.data == [0,1,None,None]
    assert queue.size == 2
    assert queue.capacity == 4
    assert queue.head == 0
    assert queue.tail == 2

    #7 greatest_val
    values = [1, 2, 3, 4]
    w = 2
    arr = (greatest_val(w, values))
    assert arr == [2,3,4]
    w = 3
    arr = (greatest_val(w, values))
    assert arr == [3,4]

    print("Circular Queue Functions All Passed!")
    
main()