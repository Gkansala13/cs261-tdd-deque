# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.
# YOUR NAME

# Hint: pip3 install llist
from pyllist import dllist

class Deque:

    def __init__(self):
        self.data=dllist([])

    def enqueue_left(self, value):
       return self.data.appendleft(value)

    def enqueue_right(self, value):
        return self.data.appendright(value)
    
    def dequeue_left(self):
        return self.data.popleft()

    def dequeue_right(self):
        return self.data.popright()

   