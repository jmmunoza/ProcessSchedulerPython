from process import Process

class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop(0)
        
    def push(self, process):
        self.stack.append(process)
        
    def get(self):
        if len(self.stack) > 0:
            return self.stack[0]
        else:
            return None
        
    def __len__(self):
        return len(self.stack)
        
    def __str__(self) -> str:
        str = ""
        for i in range(len(self.stack)):
            str += f'|P{i}={self.stack[i]}|\n'
            
        return str      