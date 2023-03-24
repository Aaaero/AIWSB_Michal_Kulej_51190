class Tour:
    def __init__(self, tree):
        self._tree = tree

    def execute(self):
        return self._tour(self._tree)

    def _tour(self, node):
        self._hook_previsit(node)
        if node.left is not None:
            self._tour(node.left)
        self._hook_inorder(node)
        if node.right is not None:
            self._tour(node.right)
        self._hook_postvisit(node)

    def _hook_inorder(self, p):
        pass

    def _hook_previsit(self, p):
        pass

    def _hook_postvisit(self, p):
        pass


class PreorderTour(Tour):
    def _hook_previsit(self, p):
        print(str(p.data), end=' ')


class InOrderTour(Tour):
    def _hook_inorder(self, p):
        print(str(p.data), end=' ')


class PostOrderTour(Tour):
    def _hook_postvisit(self, p):
        print(str(p.data), end=' ')


class ElementFound(Exception):
    pass


class ElementInTree(Tour):
    def __init__(self, tree):
        super().__init__(tree)
        self.searching_for = None

    def is_in_tree(self, num):
        self.searching_for = num
        try:
            self.execute()
        except ElementFound as e:
            return True
        else:
            return False

    def _hook_previsit(self, p):
        if p.data == self.searching_for:
            raise ElementFound()


def show_off(tree):
    print()
    print('-' * 10)
    print('pre order')
    PreorderTour(tree).execute()
    print()
    print('-' * 10)
    print('in order')
    InOrderTour(tree).execute()
    print()
    print('-' * 10)
    print('post order')
    PostOrderTour(tree).execute()