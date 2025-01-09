"""

rule : 

- the left sub-tree of a node hase a less than or  equal to its parents node's key
- the right sub-tree of a node has a key greater than or equal to its parent node's key

삽입

탐색

- inorder way
- preorder way
- postorder way

삭제 :

- node to be removeed has no child

"""

class TreeNode:

    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

    def insert(self,value):

        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.rigtt = TreeNode(value)
            else:
                self.right.inser(value)

if __name__ == "__main__":
    tree = TreeNode(10)
    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(7)
    tree.insert(22)
    tree.insert(11)
    tree.insert(8)


