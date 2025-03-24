class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self,root):
        self.root=root

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end="->")
            self.inorder(node.right)
    
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end="->")

    def preorder(self,node):
        if node:
            print(node.data,end="->")
            self.preorder(node.left)
            self.preorder(node.right)


root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.right.right=Node("E")

tree=Tree(root)
print("Inorder:")
tree.inorder(tree.root)
print("\n\nPreorder: ")
tree.preorder(tree.root)
print("\n\nPostorder:")
tree.postorder(tree.root)
