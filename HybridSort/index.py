from HybridSort.mergesort import merge_lists, split_linked_list, merge_sort, merge
from HybridSort.LinkedList import LinkedList 
from random import randint, shuffle, seed, choice

def main():
    """
    testing if everything works fine.
    1. insertion sort
    2. merge sort
    3. split linked list
    4. one linked list
    5. 100 positive numbers with duplicates
    6. 50 big numbers without duplicates
    """
    
    #1 insertion sort
    seed(321)
    orig = [randint(1000,1000000) * choice([-1,1]) for _ in range(50)]
    llist = LinkedList(orig)
    llist.insertion_sort()   
    assert llist == LinkedList(sorted(orig))
    
    #2 merge sort
    seed(321)
    assert merge(LinkedList([1,3,5]), LinkedList([2,4])) == LinkedList([1,2,3,4,5])

    #3 split linked list
    seed(321)
    assert split_linked_list(LinkedList([1,2,3])) == (LinkedList([1]), LinkedList([2,3]))

    #4 one linked list
    seed(321) 
    orig = [5,4,2,3,1,6]
    llist = merge_lists([LinkedList(orig)], 5)
    assert LinkedList(sorted(orig)) == llist

    #5 100 postive nubmers with duplicates
    seed(321)
    orig = [randint(1,30) for _ in range(100)]
    llist = merge_lists([LinkedList(orig), LinkedList([3,1,2]), LinkedList([10, 9, 8, 7])], 2)
    assert LinkedList(sorted(orig+[3,1,2,10,9,8,7]))==llist

    #6 50 big numbers without duplicates
    seed(321)
    orig = [randint(1000,1000000) * choice([-1,1]) for _ in range(50)]
    llist = merge_lists([LinkedList(orig)], 10)
    assert LinkedList(sorted(orig))==llist

    print("Hybrid Sort Functions All Pased!")

main()