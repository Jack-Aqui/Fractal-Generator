import turtle as t
class State:
    def __init__(self, x=0, y=0, angle=0):
        # Initialize position of turtle
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.angle)
    
    def __repr__(self):
        return self.__str__()

    def set_state(self, t):
        #Define coordinates and angle for turtle at current state
        self.x = t.xcor(self.x)
        self.y = t.ycor(self.y)
        self.angle = t.heading(self.angle)

class Stack:
    def __init__(self):
        self.stack = []
        # Inititalize stack

    def push(self, item):
        self.stack.append(item)
        # Add item to stack
    
    def pop(self):
        # Removes item from top of stack and raises error if stack is empty
        if self.is_empty():
            raise Exception('cannot pop empty stack')
        else:
            return self.stack.pop()

    def is_empty(self):
        # Check if stack is empty
        if self.stack == []:
            return True
        else:
            return False
        
