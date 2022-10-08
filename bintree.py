from platform import node


class Node:
    def __init__(self, key: int):
        self.key = key
        self.right = None
        self.left = None
 

class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, key: int): #inserts a new key to the search tree, no duplicates.
        if self.search(key) == True:
            return
        elif self.root == None:
            self.root = Node(key)
        else:
            self.helper_insert(key, self.root)

    def helper_insert(self, key, node):
        if key < node.key:
            if node.left != None:
                self.helper_insert(key, node.left)
            else:
                node.left = Node(key)
        else:
            if node.right != None:
                self.helper_insert(key, node.right)
            else:
                node.right = Node(key)

    def search(self, key: int): #searches the key from the search tree and returns boolean True if the value is found, False otherwise.
        if self.root != None:
            return self.helper_find(key, self.root)
        else:
            return False

    def helper_find(self, key, node):
        if key == node.key:
            return True
        elif key < node.key and node.left != None:
            return self.helper_find(key, node.left)
        elif key > node.key and node.right != None:
            return self.helper_find(key, node.right)
        else:
            return False


    def remove(self, key :int):
        if self.search(key) == False:
            return self.root
        if self.root == None:
            return self.root
        else:
            self.helper_remove(self.root, key)

    def helper_remove(self, node, key):
        if node == None:
            return self.root
        if key < node.key:
            node.left = self.helper_remove(node.left, key)
        elif key > node.key:
            node.right = self.helper_remove(node.right, key)
        else:
            if node.right == None:
                return node.left

            if node.left == None:
                return node.right
            
            node.key = self.next_in_tree(node.right)
            node.right = self.helper_remove(node.right, node.key)
        return node

    def next_in_tree(self, node):
        minimum = node.key
        while node.left != None:
            minimum = node.left.key
            node = node.left
        return minimum

    def preorder(self): #prints the content of the search tree in preorder. Implement the method using recursion.
        stack = []
        self.helper_preorder(self.root, stack)
        for i in stack:
            print(i, end=" ")
        print()
        return

    def helper_preorder(self, node, stack):
        if node == None:
            return
        stack.append(node.key)
        self.helper_preorder(node.left, stack)
        self.helper_preorder(node.right, stack)
        return

    def breadthfirst(self):
        height = self.height(self.root)
        for i in range(1, height+1):
            self.current_level(self.root, i)
        print()
        return

    def current_level(self, node, level):
        if node == None:
            return
        if level == 1:
            print(node.key, end=" ")
        elif level > 1:
            self.current_level(node.left, level-1)
            self.current_level(node.right, level-1)
        return
    
    def height(self,node):
        if node == None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height +1
            else:
                return right_height +1
            
if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6
    
    
