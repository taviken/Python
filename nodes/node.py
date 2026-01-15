from collections import deque
from typing import Union


class Node:
    def __init__(self, value: object):
        self.value = value
        self.parent = None
        self.children = deque()

    @property
    def is_leaf(self) -> bool:
        return not self.children

    @property
    def is_root(self) -> bool:
        return self.parent is None

    @property
    def is_single_link(self) -> bool:
        return len(self.children) == 1

    def add_left(self, item: Union[object, "Node"]) -> None:
        if not isinstance(item, self.__class__):
            item = self.__class__(item)
        self.children.appendleft(item)

    def add_right(self, item: Union[object, "Node"]) -> None:
        if not isinstance(item, self.__class__):
            item = self.__class__(item)
        self.children.append(item)

    def level_order_traversal(self, root=None, as_value=True):
        if root is None:
            root = self
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if as_value:
                yield node.value
            else:
                yield node

            if node.children:
                queue.extend(node.children)

    def pre_order_traversal(self, root=None, as_value=True):
        if root is None:
            root = self
        return self._dfs_traversal(root, as_value, True)

    def post_order_traversal(self, root=None, as_value=True):
        if root is None:
            root = self
        return self._dfs_traversal(root, as_value, False)

    def _dfs_traversal(self, root, as_value=True, is_preorder=True):

        if is_preorder:
            if as_value:
                yield root.value
            else:
                yield root

        if root.children:
            for child in root.children:
                yield from self._dfs_traversal(child, as_value, is_preorder)

        if not is_preorder:
            if as_value:
                yield root.value
            else:
                yield root

    def __eq__(self, other: Union[object, "Node"]):
        if issubclass(other.__class__, self.__class__):
            return self.value == other.value
        else:
            return self.value == other

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"


__all__ = [
    "Node",
]
