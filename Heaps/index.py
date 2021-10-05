from Heaps.Heap import Node, Heap, most_x_common
from string import ascii_lowercase

def test_push():
    '''
    simple push cases, requires functioning top
    '''
    heap = Heap(10)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')
    heap.push(2, 'd')
    heap.push(5, 'y')
    assert len(heap) == 5
    assert heap.top == 'd'
    assert min(heap._data[:5]) == heap._data[0]
    assert heap._data[1] < heap._data[3]
    assert heap._data[1] < heap._data[4]
    heap.push(6, 'y')
    assert heap._data[2] < heap._data[5]
    heap = Heap(2)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')  # invokes pop
    assert len(heap) == 2
    assert heap.top == 'y'
    assert [i.val for i in heap._data if i] == ['y', 'c']

def test_pop():
    '''
    simple pop cases, requires functioning top, push, empty
    '''
    heap = Heap(10)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')
    heap.push(2, 'd')
    heap.push(5, 'y')
    assert len(heap) == 5
    for i in range(len(heap)):
        assert heap.top == heap.pop()
    assert i == 4
    assert heap.empty
    heap = Heap(2)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')
    assert len(heap) == 2
    assert heap.pop() == 'y'
    assert not heap.empty

def check_min(heap, idx, lhs=None, rhs=None):
    '''
    function helper for validating the min method
    '''
    min_child = lhs if heap._data[lhs] < heap._data[rhs] else rhs
    assert min_child == heap._min_child(idx)

def test_min_child():
    '''
    simple min child test, requires push
    '''
    heap = Heap(10)
    for child in ascii_lowercase:
        heap.push(ord(child), child)
    assert len(heap) == 10
    check_min(heap, 0, 1, 2)
    check_min(heap, 2, 5, 6)
    check_min(heap, 3, 7, 8)
    
def test_levels():
    '''
    simple levels cases, requires functioning pop and push
    '''
    heap = Heap(6)
    for child in ascii_lowercase[:6]:
        heap.push(ord(child), child)
    answer = [
        [Node(97, 'a')],
        [Node(98, 'b'), Node(99, 'c')],
        [Node(100, 'd'), Node(101, 'e'), Node(102, 'f')]
    ]
    assert heap.levels == answer
    heap.pop()
    answer = [
        [Node(98, 'b')],
        [Node(100, 'd'), Node(99, 'c')],
        [Node(102, 'f'), Node(101, 'e')]
    ]
    assert heap.levels == answer
    
def test_most_x():
    '''
    general application cases
    '''
    result = most_x_common(['a', 'a', 'a', 'b', 'b', 'c'], 2)
    assert result == set('ab')
    result = most_x_common(['a', 'a', 'a', 'b', 'b', 'b', 'c'], 3)
    assert result == set('abc')
    result = most_x_common(list('a' * 99 + 'b'), 1)
    assert result == {'a'}

def main():
    """
    testing if everything works fine.
    1. push
    2. pop
    3. min_child
    4. levels
    5. most_x_common
    """
    
    test_push()
    test_pop()
    test_min_child()
    test_levels()
    test_most_x()
    
    print("Heaps Functions All Passed!")
    
main()

