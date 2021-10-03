from HybridSort.LinkedList import LinkedList

def merge_lists(lists, threshold):
    """
    sort and combine every linkedlist in lists
    :param lists: given lists
    :param threshold: user insertion sort if it is less than this
    :return: final linked list
    """
    new_list = LinkedList()
    counter = 0
    while counter < len(lists):
        lists[counter] = merge_sort(lists[counter], threshold)
        counter += 1
    for j in lists:
        new_list = merge(new_list, j)
    return new_list

def merge_sort(linked_list, threshold):
    """
    user merge sort to sort the given linked list
    :param linked_list: given linked list
    :param threshold: use the insertion sort if linked list is smaller
    :return: sorted list
    """
    if linked_list.length() < 2:
        return linked_list

    elif linked_list.length() <= threshold:
        linked_list.insertion_sort()
        return linked_list

    else:
        first_split = split_linked_list(linked_list)
        tuple1 = merge_sort(first_split[0], threshold)
        tuple2 = merge_sort(first_split[1], threshold)
    return merge(tuple1, tuple2)

def split_linked_list(linked_list):
    """
    take a linked list and split in half
    :param linked_list: given linked list
    :return: tuple of two split lists
    """
    l = linked_list.length()
    first = LinkedList()
    if l % 2 == 1:
        for i in range(1, l//2+1):
            first.push_back(linked_list.pop_front())
    else:
        while first.length() != linked_list.length():
            first.push_back(linked_list.pop_front())
    return tuple([first, linked_list])


def merge(list1, list2):
    """
    merges two sorted linked lists
    :param list1: first list
    :param list2: second list
    :return: one sorted linked list
    """
    new = LinkedList()

    while list1 or list2:
        front1 = list1.front_value()
        front2 = list2.front_value()
        if list1.length() == 0:
            new.push_back(list2.pop_front())
            continue
        if list2.length() == 0:
            new.push_back(list1.pop_front())
            continue

        if front1 < front2:
            new.push_back(front1)
            list1.pop_front()
        elif front1 > front2:
            new.push_back(front2)
            list2.pop_front()
        elif front1 == front2:
            new.push_back(front1)
            list1.pop_front()
            new.push_back(front2)
            list2.pop_front()
    return new
