def inorder_traversal(root):
    node_val_list = []
    node_list = []
    while root or node_list:
        while root:
            node_list.append(root)
            root = root.left
        root = node_list.pop()
        node_val_list.append(root.val)
        root = root.right
    return node_val_list
