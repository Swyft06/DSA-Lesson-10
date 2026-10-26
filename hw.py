class BinarySearchTree:
    def __init__(self,v):
        self.data = v
        self.left = None
        self.right = None


def Insert(root,k):
    if root == None:
        return BinarySearchTree(k)
    if k< root.data:
        root.left = Insert(root.left,k)

    else:
        root.right = Insert(root.right,k)

    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)

    if root.data % 2 == 0:
        print(root.data)

    inorder(root.right)

n = int(input("Enter the number of elements for the tree: "))
root = None

for i in range(n):
    a = int(input("Enter the value for the nodes: "))
    root = Insert(root,a)
print(inorder(root))