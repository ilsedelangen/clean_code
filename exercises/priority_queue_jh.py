from numbers import Number
from typing import Hashable, Sized


class IllegalStateError(RuntimeError):
    """Custom error class to give the error more context"""
    # No implementation needed, as we inherit everything we need
    # (except for the type) from RuntimeError
    pass


class PriorityQueue:
    """Example implementation of the Priority Queue Kata"""

    def __init__(self, max_elements: int = 10):
        self._max_elements = max_elements
        self._queue = {}

    def push(self, element: object, weight: Hashable = 1) -> None:
        """Add new elements to the queue"""
        if len(self) >= self._max_elements:
            raise IllegalStateError('Size limit reached')

        if weight not in self._queue:
            self._queue[weight] = []
        self._queue[weight].append(element)

    def pop(self) -> object:
        """Get the element with the highest weight"""
        return self._extract_first_element(self._find_highest_subqueue())

    def _find_highest_subqueue(self) -> list:
        for sq in self._get_queues_sorted():
            if sq: return sq
        return None

    def _get_queues_sorted(self) -> list:
        keys = list(self._queue.keys())
        keys.sort(key=lambda x: sort_arb_values(x), reverse=True)
        return [self._queue[k] for k in keys]

    def _get_subqueue_for_key(self, key: Hashable):
        return self._queue[key]

    @staticmethod
    def _extract_first_element(subqueue: list) -> object:
        return subqueue.pop(0)

    def __len__(self):
        return sum(len(v) for v in self._queue.values())


def sort_arb_values(obj: object):
    if isinstance(obj, Number):
        return obj
    elif isinstance(obj, Sized):
        return len(obj)
    else:
        return 0
