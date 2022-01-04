
#https://www.techiedelight.com/stack-implementation-python/

class Stack():

    #constructor
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    def push(self, x):
        if self.isFull():
            print("Stack Overflow!! Calling exit()…")
            exit(1)
        print("Inserting", x, "into the stack…")
        self.top =self.top+1
        self.arr[self.top] =  x


    #function to pop top elements
    def pop(self):
        #check for stack underflow
        if self.isEmpty():
            print("Stack Underflow!! Calling exit()…")
            exit(1)

        print("Removing", self.peek(), "from the stack")
        # decrease stack size by 1 and (optionally) return the popped element
        top = self.arr[self.top]

        self.top = self.top -1
        return top 

    # Function to return the top element of the stack
    def peek(self):
        if self.isEmpty():
            exit(1)
        return self.arr[self.top]
    

    # Function to return the size of the stack
    def size(self):
        return self.top + 1

    # Function to check if the stack is empty or not
    def isEmpty(self):
        return self.size() == 0
 
    # Function to check if the stack is full or not
    def isFull(self):
        return self.size() == self.capacity
 

if __name__ == '__main__':
 
    stack = Stack(3)
 
    stack.push(1)       # Inserting 1 in the stack
    stack.push(2)       # Inserting 2 in the stack
 
    stack.pop()         # removing the top element (2)
    stack.pop()         # removing the top element (1)
 
    stack.push(3)       # Inserting 3 in the stack
 
    print("Top element is", stack.peek())
    print("The stack size is", stack.size())
 
    stack.pop()         # removing the top element (3)
 
    # check if the stack is empty
    if stack.isEmpty():
        print("The stack is empty")
    else:
        print("The stack is not empty")





# using deque
    from collections import deque
 
 
    stack = deque()
 
    print("Inserting 'A' into the stack…")
    stack.append('A')
 
    print("Inserting 'B' into the stack…")
    stack.append('B')
 
    print("Inserting 'C' into the stack…")
    stack.append('C')
 
    print("Inserting 'D' into the stack…")
    stack.append('D')
 
    print("Top element is", stack[-1])                 # prints the stack's top (`D`)
 
    print("Removing", stack.pop(), "from the stack")   # removing the top element (`D`)
    print("Removing", stack.pop(), "from the stack")   # removing the next top (`C`)
 
    # returns the total number of elements present in the stack
    print("The stack size is", len(stack))
 
    print("Removing", stack.pop(), "from the stack")   # removing the top element (`B`)
    print("Removing", stack.pop(), "from the stack")   # removing the next top (`A`)
 
    # check if the stack is empty
    if len(stack) == 0:
        print("The stack is empty")
    else:
        print("The stack is not empty")
