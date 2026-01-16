from collections import deque
from typing import Union, IO
from io import StringIO
from pprint import pprint


def _to_dict(node: "Node") -> dict:
    d = {"value": node.value}
    if node.children:
        d["children"] = [_to_dict(child) for child in node.children]
    return d


def _format_tree_with_pipes(node: "Node", stream: IO, prefix="", is_last=True):
    # Connector for the current node
    connector = "└── " if is_last else "├── "
    print(f"{prefix}{connector}{node.value}", file=stream)

    # Prepare prefix for children
    new_prefix = prefix + ("    " if is_last else "│   ")

    # Iterate through children and recurse
    temp = list(reversed(node.children))
    while temp:
        child = temp.pop()
        _format_tree_with_pipes(child, stream, new_prefix, not bool(temp))


class Node:
    def __init__(self, value: object):
        self.value = value
        self.parent = None
        self.children = deque()

    @property
    def is_leaf(self) -> bool:
        return not self.children

    @property
    def is_binary(self) -> bool:
        return len(self.children) == 2

    @property
    def is_root(self) -> bool:
        return self.parent is None

    @property
    def is_single_link(self) -> bool:
        return len(self.children) == 1

    @property
    def as_dict(self) -> dict:
        return _to_dict(self)

    def add_left(self, item: Union[object, "Node"]) -> None:
        if not isinstance(item, self.__class__):
            item = self.__class__(item)

        item.parent = self
        self.children.appendleft(item)

    def add_right(self, item: Union[object, "Node"]) -> None:
        if not isinstance(item, self.__class__):
            item = self.__class__(item)
        item.parent = self
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

    def find_greedy(self, item, as_value=True):
        for node in self.pre_order_traversal(as_value=as_value):
            if node == item:
                yield node

    def find_lazy(self, item, as_value=True):
        for node in self.pre_order_traversal(as_value=as_value):
            if node == item:
                return node

    def __eq__(self, other: Union[object, "Node"]):
        if issubclass(other.__class__, self.__class__):
            return self.value == other.value
        else:
            return self.value == other

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"

    def __format__(self, format_spec):
        if format_spec == "pipe":
            stream = StringIO()
            _format_tree_with_pipes(self, stream)
            return stream.getvalue()
        elif format_spec == "dict":
            stream = StringIO()
            pprint(self.as_dict, stream)
            return stream.getvalue()


__all__ = [
    "Node",
]
