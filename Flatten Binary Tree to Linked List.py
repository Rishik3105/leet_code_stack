class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def flatten(root):
    def helper(node):
        if not node:
            return None
        left_tail = helper(node.left)
        right_tail = helper(node.right)
        if node.left:
            if left_tail:
                left_tail.right = node.right
            node.right = node.left
            node.left = None
        return right_tail or left_tail or node
    helper(root)
