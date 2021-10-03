from AVL_Trees.AVLTree import Node, AVLTree, repair_tree

def main():
    """
    testing if everything works fine.
    1. left and right rotate
    2. insert
    3. search
    4. remove
    5. traversals
    6. depth/height
    7. min/max
    8. repair tree
    9. all
    """

    #1 left and right rotate
    avl = AVLTree()
    avl.root = Node(3)
    avl.root.left = Node(2, parent=avl.root)
    avl.root.left.left = Node(1, parent=avl.root.left)
    avl.size = 3
    avl.right_rotate(avl.root)
    assert avl.root.value == 2
    assert avl.root.left.value == 1
    assert avl.root.right.value == 3
    avl2 = AVLTree()
    avl2.root = Node(1)
    avl2.root.right = Node(2, parent=avl2.root)
    avl2.root.right.right = Node(3, parent=avl2.root.right)
    avl2.size = 3
    avl2.left_rotate(avl2.root)
    assert avl2.root.value == 2
    assert avl2.root.left.value == 1
    assert avl2.root.right.value == 3

    #2 insert
    avl = AVLTree()
    avl.insert(avl.root, 5)
    avl.insert(avl.root, 10)
    avl.insert(avl.root, 1)
    avl.insert(avl.root, 3)
    avl.insert(avl.root, 7)
    assert avl.root.value == 5
    assert avl.root.left.value == 1
    assert avl.root.left.right.value == 3
    assert avl.root.right.value == 10
    assert avl.root.right.left.value == 7
    avl2 = AVLTree()
    avl2.insert(avl2.root, 3)
    avl2.insert(avl2.root, 2)
    avl2.insert(avl2.root, 1)
    avl2.insert(avl2.root, 4)
    avl2.insert(avl2.root, 5)
    assert avl2.root.value == 2
    assert avl2.root.left.value == 1
    assert avl2.root.right.value == 4
    assert avl2.root.right.left.value == 3
    assert avl2.root.right.right.value == 5
    avl3 = AVLTree()
    avl3.insert(avl3.root, 1)
    avl3.insert(avl3.root, 5)
    avl3.insert(avl3.root, 2)
    avl3.insert(avl3.root, 9)
    avl3.insert(avl3.root, 10)
    avl3.insert(avl3.root, 20)
    avl3.insert(avl3.root, 7)
    assert avl3.root.value == 9
    assert avl3.root.left.value == 2
    assert avl3.root.left.left.value == 1
    assert avl3.root.left.right.value == 5
    assert avl3.root.left.right.right.value == 7
    assert avl3.root.right.value == 10
    assert avl3.root.right.right.value == 20

    #3 search
    avl = AVLTree()
    avl.insert(avl.root, 30)
    avl.insert(avl.root, 20)
    avl.insert(avl.root, 40)
    avl.insert(avl.root, 10)
    avl.insert(avl.root, 25)
    avl.insert(avl.root, 35)
    avl.insert(avl.root, 50)
    assert avl.search(avl.root, 10) == avl.root.left.left
    assert avl.search(avl.root, 50) == avl.root.right.right
    assert avl.search(avl.root, 20) == avl.root.left

    #4 remove
    avl = AVLTree()
    avl.insert(avl.root, 10)
    avl.insert(avl.root, 5)
    avl.insert(avl.root, 15)
    avl.insert(avl.root, 1)
    avl.insert(avl.root, 7)
    avl.insert(avl.root, 13)
    avl.insert(avl.root, 19)
    avl.remove(avl.root, 7)
    assert avl.root.left.right == None
    avl.remove(avl.root, 1)
    assert avl.root.left.left == None
    avl.remove(avl.root, 5)
    assert avl.root.value == 15
    assert avl.root.left.value == 10
    assert avl.root.right.value == 19
    assert avl.root.left.right.value == 13

    #5 traversals
    avl = AVLTree()
    avl.insert(avl.root, 14)
    avl.insert(avl.root, 7)
    avl.insert(avl.root, 21)
    avl.insert(avl.root, 3)
    avl.insert(avl.root, 10)
    avl.insert(avl.root, 17)
    avl.insert(avl.root, 25)
    gen1 = avl.preorder(avl.root)
    gen2 = avl.postorder(avl.root)
    gen3 = avl.inorder(avl.root)
    pre = [14,7,3,10,21,17,25]
    post = [3,10,7,17,25,21,14]
    inorder = sorted(post)
    for i in range(7):
        assert next(gen1, None).value == pre[i]
        assert next(gen2, None).value == post[i]
        assert next(gen3, None).value == inorder[i]
    
    #6 depth/height
    avl = AVLTree()
    avl.insert(avl.root, 21)
    avl.insert(avl.root, 10)
    avl.insert(avl.root, 32)
    avl.insert(avl.root, 5)
    avl.insert(avl.root, 16)
    avl.insert(avl.root, 27)
    avl.insert(avl.root, 39)
    assert avl.depth(5) == 2
    assert avl.depth(10) == 1
    assert avl.height(avl.root) == 2
    assert avl.height(avl.root.left) == 1

    #7 min/max
    avl = AVLTree()
    avl.insert(avl.root, 10)
    avl.insert(avl.root, 5)
    avl.insert(avl.root, 15)
    avl.insert(avl.root, 3)
    avl.insert(avl.root, 8)
    avl.insert(avl.root, 12)
    avl.insert(avl.root, 18)
    assert avl.min(avl.root).value == 3
    assert avl.max(avl.root).value == 18

    #8 repair tree
    avl = AVLTree()
    correct = AVLTree()
    avl.insert(avl.root, 10)
    correct.insert(correct.root, 10)
    avl.insert(avl.root, 5)
    correct.insert(correct.root, 5)
    avl.insert(avl.root, 15)
    correct.insert(correct.root, 15)
    avl.insert(avl.root, 3)
    correct.insert(correct.root, 3)
    avl.insert(avl.root, 7)
    correct.insert(correct.root, 7)
    avl.insert(avl.root, 12)
    correct.insert(correct.root, 12)
    avl.insert(avl.root, 18)
    correct.insert(correct.root, 18)
    avl.root.left.value, avl.root.right.value = avl.root.right.value, avl.root.left.value
    repair_tree(avl)
    assert avl == correct

    #9 all
    avl = AVLTree()
    insert_list = [50,3,15,20,18,63,75,100,148,47,68,9,71,33]
    remove_list = [68,75,20,63]
    for i in insert_list:
        avl.insert(avl.root, i)

    for i in remove_list:
        avl.remove(avl.root, i)

    assert avl.root.value == 18
    assert avl.depth(avl.search(avl.root, 33).value) == 3
    assert avl.height(avl.root) == 3
    assert avl.max(avl.root) == avl.root.right.right.right
    gen1 = avl.inorder(avl.root)
    correct = sorted([item for item in insert_list if item not in remove_list])
    for i in range(len(correct)):
        assert next(gen1, None).value == correct[i]
    assert avl.get_balance(avl.root.right) == 0
    
    print("AVL Tree Functions All Passed!")
    
main()