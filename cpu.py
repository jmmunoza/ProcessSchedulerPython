from stack import Stack
from process import Process
import sys, time 

class CPU:
    def __init__(self, args=[]):
        
        stack = Stack()
        
        n_processes = len(args) // 2
        for i in range(n_processes):
            process = Process(args[2*i], args[(2*i)+1])
            stack.push(process)
        
        init_time = time.time()
        while len(stack) > 0:
            process = stack.get()
            process.run()

            if process.time < time.time() - init_time:
                init_time = time.time()
                stack.pop()

# & C:/Users/User/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/User/Desktop/Semestre 7/Sistemas Operativos/ProcessScheduler/cpu.py" "Proceso 1" 3 "Proceso 2" 3 "Proceso 3" 8 "Proceso 4" 6 "Proceso 5" 3 "Proceso 6" 2 "Proceso 7" 1      
if __name__ == '__main__':
    args = sys.argv[1:]
    cpu = CPU(args)       