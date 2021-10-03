from Algorithms.LinkedList import LinkedList

def main():
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    assert str(llist) == "[1, 2, 3, 4]"
    
if __name__ == '__main__':
    main()