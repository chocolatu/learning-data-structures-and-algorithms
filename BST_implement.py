import queue

class BST:
    class Node:
        # Node's init function
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    # BST's init function
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            # curr points to the variable we are currently looking at
            curr = self.root
            inserted = False

            while not inserted:
                if data < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = BST.Node(data)
                        inserted = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(data)
                        inserted = True

    def search(self, data):
        curr = self.root

        while curr is not None:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr

        return None

    def breadth_first_print(self):
        the_nodes = queue.Queue()

        if self.root is not None:
            the_nodes.put(self.root)

        while not the_nodes.empty():
            curr = the_nodes.get()

            if curr.left:
                the_nodes.put(curr.left)
            if curr.right:
                the_nodes.put(curr.right)

            print(curr.data, end=" ")

    # recursive search
    def r_search(self, data, subtree):
        if subtree is None:
            return None
        else:
            if data < subtree.data:
                return self.r_search(data, subtree.left)
            elif data > subtree.data:
                return self.r_search(data, subtree.right)
            else:
                return subtree

    def search_recursive(self, data):
        return self.r_search(data, self.root)

    # recursive insert
    def ins(self, data, subtree):
        if (subtree == None):
            return BST.Node(data)
        elif (data < subtree.data):
            subtree.left = self.ins(data, subtree.left)
            return subtree
        else:
            subtree.right = self.ins(data, subtree.right)
            return subtree

    def recursive_insert(self, data):
        self.root = self.ins(data, self.root)

    # inorder print: left, node, right
    def print_inorder(self, subtree):
        if (subtree != None):
            self.print_inorder(subtree.left)
            print(subtree.data, end=" ")
            self.print_inorder(subtree.right)

    def print(self):
        self.print_inorder(self.root)
        print("")

    # preorder print: node, left, right
    def print_preorder(self, subtree):
        if (subtree != None):
            print(subtree.data, end=" ")
            self.print_preorder(subtree.left)
            self.print_preorder(subtree.right)

    def print(self):
        self.print_preorder(self.root)
        print("")