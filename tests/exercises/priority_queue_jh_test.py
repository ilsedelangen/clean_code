import pytest

from ...exercises.priority_queue_jh import PriorityQueue, IllegalStateError


def test_empty_creation():
    assert len(PriorityQueue()) == 0


def test_queue_somthing():
    queue = PriorityQueue()
    queue.push(None)
    assert len(queue) == 1


def test_arbitrary_weight():
    queue = PriorityQueue()
    queue.push('a', 'asd')
    queue.push('c', 3.141)
    queue.push('c', 3)
    assert len(queue) == 3


def test_dequeue():
    queue = PriorityQueue()
    queue.push('a', 'asd')
    assert queue.pop() == 'a'


def test_dequeue_order():
    queue = PriorityQueue()
    queue.push('a', 'asd')
    queue.push('b', 4)
    queue.push('c', 1.23)
    assert queue.pop() == 'b'
    assert queue.pop() == 'a'
    assert queue.pop() == 'c'


def test_dequeue_order_same_weight():
    queue = PriorityQueue()
    queue.push('a', 1)
    queue.push('b', 2)
    queue.push('c', 1)
    assert queue.pop() == 'b'
    assert queue.pop() == 'a'
    assert queue.pop() == 'c'


def test_limit():
    queue = PriorityQueue(max_elements=1)
    queue.push('c', 1)
    with pytest.raises(IllegalStateError):
        queue.push('c', 1)
