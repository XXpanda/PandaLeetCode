def preorder_traversal(root):
    node_val_list = []
    node_list = []
    while root or node_list:
        while root:
            node_list.append(root)
            node_val_list.append(root.val)
            root = root.left
        root = node_list.pop()
        root = root.right
    return node_val_list
