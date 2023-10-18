'''
This code defines a stack class that allows you to perform basic stack operations such as push, pop, peek, and flush. 
The `__init__` method initializes the stack with a specified maximum size.
The `is_empty` method checks if the stack is empty by checking the length of the stack list. If it is empty, it prints a message and returns True. Otherwise, it returns False.
The `is_full` method checks if the stack is full by comparing the length of the stack list to the capacity. If it is full, it prints a message and returns True. Otherwise, it returns False.
The `flush` method clears the stack by assigning an empty list to the stack attribute. It first checks if the stack is not empty before performing the operation.
The `peek` method returns the value at the top of the stack without removing it. It checks if the stack is not empty before printing the value.
The `pop` method removes the value at the top of the stack. It checks if the stack is not empty before removing the value.
The `push` method adds a new value to the top of the stack. It checks if the stack is not full before adding the value.
The `view_stack` method displays all the values in the stack, starting from the top. It checks if the stack is empty before iterating over the stack list and printing each value.
The `__name__ == "__main__"` block is executed when the script is run directly (not imported as a module). It prompts the user to enter the maximum size of the stack and creates an instance of the stack class.
It then enters a while loop that repeatedly displays the current stack, prompts the user for a choice, and performs the corresponding operation based on the choice. The loop continues until an invalid choice is made.
'''


class stack:

    def __init__(self, maxSize):
        self.capacity = maxSize
        self.stack = []

    def is_empty(self):
        if len(self.stack) is 0:
            print('[i] Stack is empty')
            return True
        else:
            return False

    def is_full(self):
        if len(self.stack) is self.capacity:
            print('[i] Stack is full')
            return True
        else:
            return False

    def flush(self):
        if not self.is_empty():
            self.stack = []

    def peek(self):
        if not self.is_empty():
            print(f'[~] Value received {self.stack[-1]}')

    def pop(self):
        if not self.is_empty():
            self.stack = self.stack[:-1]

    def push(self, data):
        if not self.is_full():
            self.stack.append(data)

    def view_stack(self):
        if self.is_empty(): return
        for data in reversed(self.stack):
            print(f'- {data}')

if __name__ == "__main__":
    pystack = stack(int(input('Max Size: ')))
    while 1:
        pystack.view_stack()
        choice = int(input('[1] Push | [2] Peak | [3] Pop | [4] Flush\n---\n> Choice: '))
        if choice == 1:
            data = input('Data: ')
            pystack.push(data)
                
        elif choice == 2:
            pystack.peek()

        elif choice == 3:
            pystack.pop()

        elif choice == 4:
            pystack.flush()
        else:
            print('Invalid Choice')
        
