# Program: Calculator 
# author: Manusri Allam
# date: 3/6/2023
'''
# file: Calculator is a program that takes an expression from the user, then does infix to postfix conversion,
makes a tree using stack functionality to organize the various operators and operands. Finally does the calculation
and returns the final answer to the expression. The programn gets advanced by implementing a GUI (a global user interface)
'''
# input: Inputs that are given by the user is the expression to evaluate by the calculator program
# output: It outputs an answer as a float to the given expression provided by the user.

#This is the class Stack
class Stack:
    #initializes items into like a list like format
    def __init__(self):
        self.items = []
    
    #checks if there are no items in like the stack
    def isEmpty(self):
        return self.items == []
    #appends the item to the stack
    def push(self, item):
        self.items.append(item)
    #It pops the item from the stack
    def pop(self):
        return self.items.pop()
    #checks if the length of the items equal to zero, if so returns zero
    #Finally returns the last item if there are more than zero items
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# a driver program for class Stack

'''
This is the driver code for stack class. It checks if all methods are working correctly.
And if it is not, when the file is run, it throws an error.
'''
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
