class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data) + " (" + str(self.left) + ")(" + str(self.right) + ")"


def treeify(wezly):
    return _treeify(wezly, None, 0)


def _treeify(wezly, root, i):
    if i < len(wezly):
        new_root = Node(wezly[i])
        root = new_root
        root.left = _treeify(wezly, root.left, 2 * i + 1)
        root.right = _treeify(wezly, root.right, 2 * i + 2)
    return root
