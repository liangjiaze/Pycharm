class TreeNode:
    def __init__(self,val = None, left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
    def settag(self,tag = None):
        self.tag = tag

def visit(treenode):
    print(str(treenode.val),end=' ')
