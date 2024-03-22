# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:16:11 2024

@author: ilsed
"""
import numpy as np
import random

class IllegalStateError(RuntimeError):
    pass

class PriorityQueue():
    
    def __init__(self, size_limit = 100):
        self.queue = {} 
        self.FIRST_QUEUED_ITEM = 0
        self.size_limit = size_limit
        
    def check_size_limit(self):
        if self.determine_size() > self.size_limit:
            return True
        else:
            return False
         
    def add_to_queue(self, element, weight): 
        if weight in self.queue.keys():
            self.queue[weight].append(element)
        else:
            self.queue[weight] = [element]   
        if self.check_size_limit():
            raise IllegalStateError("Size limit reached")
        
    def determine_size(self):
        return sum([len(value) for value in self.queue.values()])
    
    def get_weight_for_deletion(self):
        weight_for_deletion = max(self.queue.keys())
        return weight_for_deletion
    
    def dequeue(self):
        weight_for_deletion = self.get_weight_for_deletion()
        self.queue[weight_for_deletion].pop(self.FIRST_QUEUED_ITEM)
        if len(self.queue[weight_for_deletion]) == 0: 
            del(self.queue[weight_for_deletion]) 
        
     

    
    
        
        
    