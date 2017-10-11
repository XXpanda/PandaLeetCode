# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''
    思路：利用广度优先搜索，得到需要插入的行，然后对其进行操作。
    '''
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(v)
        if d == 1:
            result_root = TreeNode(v)
            result_root.left = root
            return result_root
        node_list = [root]
        current_depth = 2
        while node_list:
            temp_list = []
            if current_depth == d:
                for node in node_list:
                    if node.left:
                        temp = node.left
                        node.left = TreeNode(v)
                        node.left.left = temp
                        temp_list.append(node.left)
                    else:
                        node.left = TreeNode(v)
                    if node.right:
                        temp = node.right
                        node.right = TreeNode(v)
                        node.right.right = temp
                        temp_list.append(node.right)
                    else:
                        node.right = TreeNode(v)
                break
            else:
                for node in node_list:
                    if node.left:
                        temp_list.append(node.left)
                    if node.right:
                        temp_list.append(node.right)
            node_list = temp_list
            current_depth += 1
        return root