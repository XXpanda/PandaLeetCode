# coding=utf-8

def preorder_traversal(root):
    '''
    后续遍历主要问题是要记住操作节点时，该节点的情况
    :param root:
    :return:
    '''
    node_val_list = []
    p = root
    node_list = [p]
    pre_node = root
    while node_list:
        top = node_list[-1]
        if (not top.left and not top.right) or (not top.right and top.left) or (pre_node == top.right):
            node_val_list.append(top.val)
            pre_node = top
            node_list.pop()
        else:
            if top.right:
                node_list.append(top.right)
            if top.left:
                node_list.append(top.left)
    return node_val_list
