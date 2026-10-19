class Tree:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def InOrderTraversal(root):
    if root:
        if root.left:
            InOrderTraversal(root.left)
        print(root.data)
        if root.right:
            InOrderTraversal(root.right)

def Insert(root,k):
    if root == None:
        return Tree(k)

    if k < root.data:
        root.left = Insert(root.left,k)

    else:
        root.right = Insert(root.right,k)

    return root

def Search(root,key):
    if root.data == key:
        return root
    elif key < root.data and root.left is not None:
        return Search(root.left,key)
    elif key > root.data and root.right is not None:
        return Search(root.right,key)
    else:
        return -1


n = int(input("Enter number of elements in the node: "))
root = None

for i in range(n):
    a = int(input("Enter the value for the node: "))
    root = Insert(root,a)

InOrderTraversal(root)


x = int(input("Enter the number you want to search: "))
t = Search(root,x)
if t == -1:
    print("Number does not exist in the tree")
else:
    print("Number exists in the tree",t.data)