from collections import deque
from typing import Generic, TypeVar
T = TypeVar("T")

class BoundedBuffer(Generic[T]):
    """FIFO buffer that rejects writes when full."""
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._items: deque[T] = deque()
        self.capacity = capacity

    def put(self, item: T) -> bool:
        if len(self._items) >= self.capacity:
            return False
        self._items.append(item)
        return True

    def get(self) -> T | None:
        return self._items.popleft() if self._items else None

    def __len__(self) -> int:
        return len(self._items)
