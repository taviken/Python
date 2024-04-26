from collections import deque
from dataclasses import dataclass
from typing import TypeVar, Any, Optional, Deque

N = TypeVar("N", bound="Node")


def _find_value_bfs(node: N, value: Any) -> Optional[N]:
    while node.children:
        child = node.children.popleft()
        if child.value == value:
            return child
        if child.children:
            _find_value_bfs(child, value)


class Node:
    value: Any
    children: Deque[N] = None

    def _post_init__(self) -> None:
        self.children = deque([]) if self.children is None else self.children

    def add_left(self, child: N) -> None:
        self.children.appendleft(child)

    def add_right(self, child: N) -> None:
        self.children.append(child)

    def bfs(self, value: Any) -> Optional[N]:
        return self._find_value_bfs(self, value)
