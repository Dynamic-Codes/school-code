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
            print(f'[~] Value recieved {self.stack[-1]}')

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
        
