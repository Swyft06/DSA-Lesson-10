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

def min(root):
    while root.left is not None:
        root = root.left
    return root.data

def max(root):
    while root.right is not None:
        root = root.right
    return root.data

def sum(root):
    if root.left is not None and root.right is not None:
        return root.data
    



n = int(input("Enter the number of elements for the tree: "))
root = None

for i in range(n):
    a = int(input("Enter the value for the nodes: "))
    root = Insert(root,a)


print("The minimum value is: ",min(root))
print("The maximum value is: ",max(root))