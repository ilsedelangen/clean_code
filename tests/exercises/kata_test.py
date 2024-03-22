# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:17:09 2024

@author: ilsed
"""

from ...exercises.kata import PriorityQueue, IllegalStateError
import random
import pytest

def test_add_to_queue():
    test_queue = PriorityQueue()
    test_queue.add_to_queue(1,2)
    test_queue.add_to_queue(2,4)
    test_queue.add_to_queue(6,1) 
    test_queue.add_to_queue(7,1)      
    assert [*test_queue.queue.values()] == [[1],[2],[6,7]]
    
def test_empty_queue():
    test_queue_empty = PriorityQueue()
    assert test_queue_empty.determine_size() == 0
    
def test_determine_size():
    test_queue = PriorityQueue()
    test_queue.add_to_queue(1,4)
    test_queue.add_to_queue("string", 6)
    test_queue.add_to_queue(6, 8)
    assert test_queue.determine_size() == 3
    
def test_dequeue_descending_order():
    test_queue = PriorityQueue()
    test_queue.add_to_queue(1,2)
    test_queue.add_to_queue(2,4)
    test_queue.add_to_queue(6,1)
    test_queue.add_to_queue(7,4)
    test_queue.dequeue() 
    assert [*test_queue.queue.values()] == [[1],[7],[6]]  
    
def test_size_limit():
    test_queue = PriorityQueue(size_limit=3)
    test_queue.add_to_queue(1,2)
    test_queue.add_to_queue(2,4)
    test_queue.add_to_queue(6,1)
    with pytest.raises(IllegalStateError):
        test_queue.add_to_queue(8,1)

    

    
    
    

    
    