class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        if t.left or t.right:
            left = '({})'.format(self.tree2str(t.left))
        else:
            left = ''
        if t.right:
            right = '({})'.format(self.tree2str(t.right))
        else:
            right = ''
        return '{}{}{}'.format(t.val, left, right)


if __name__ == '__main__':
    root = TreeNode(100)
    root.left = TreeNode(1)
    root.right = TreeNode(10)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(20)
    root.right.left = TreeNode(30)
    root.right.left.right = TreeNode(50)
    solution = Solution()
    print solution.tree2str(root)