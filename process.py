import time as tm

class Process:
    def __init__(self, args=None, time=1):
        self.args = args
        self.time = float(time)
    
    def run(self):
        print(self.args)
        
    def __str__(self):
        return f'{self.args}, T={self.time}s'