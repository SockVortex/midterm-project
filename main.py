class Process:
    def __init__(self, pid, priority, task, time):
        self.pid = pid
        self.priority = priority
        self.task = task
        self.time = time

    def __str__(self):
        return f"Process({self.pid})"

class Node:
    def __init__(self, process):
        self.process = process
        self.next = None
    def get_process(self):
        return self.process
    def __str__(self):
        return f"Process({self.process})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, process):
        new_process = Node(process)
        if self.tail is None:
            self.tail = new_process
            self.head = new_process
        else:
            self.tail.next = new_process
            self.tail = self.tail.next
    
    def remove(self):
        if (self.head is not None):
            process = self.head
            self.head = self.head.next
            return process
        else:
            return None
    
    def getAllProcesses(self):
        processes = []
        current = self.head
        while current is not None:
            processes.append(current.get_process())
            current = current.next
        return processes

class Stack:
    def __init__(self):
        self._size = 0
        self.process_list = LinkedList()
        
    def push(self, process):
        new_process = Node(process)
        new_process.next = self.process_list.head
        self.process_list.head = new_process
        if self.process_list.tail is None:
            self.process_list.tail = new_process
        self._size += 1

    def pop(self): 
        if self.process_list.head is not None:
            process = self.process_list.head.get_process()
            if self.process_list.head == self.process_list.head.next:
                self.process_list.tail = None
                if self.process_list.head is not None:
                    self.process_list.tail = None
                self._size -= 1
            return process
        return None

    def getAllProcesses(self):
        return self.process_list.getAllProcesses()

class Queue:
    def __init__(self):
        self._size = 0
        self.process_list = LinkedList()
        
    def enqueue(self, process):
        self.process_list.append(process)
        self._size += 1
   
    def dequeue(self):
        if not self.is_empty():
            process = self.process_list.remove()
            if process is not None:
                self._size -= 1
                return process.get_process() if process else None
        return None
    
    def is_empty(self):
        return self.process_list.head is None

    def peek(self):
        if not self.is_empty():
            return self.process_list.head.get_process()
        return None
    
    def getAllProcesses(self):
        processes = []
        current = self.process_list.head
        while current is not None:
            processes.append(current.get_process())
            current = current.next
        return processes

def priority_scheduler(processes):
    """Sort processes based on priority (lower number = higher priority)"""
    # Using merge sort for sorting
    if len(processes) <= 1:
        return processes
    
    mid = len(processes) // 2
    left = priority_scheduler(processes[:mid])
    right = priority_scheduler(processes[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists based on priority and time"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # Lower priority number = higher priority
        # If same priority, sort by time (smaller time first)
        if (left[i].priority < right[j].priority or 
            (left[i].priority == right[j].priority and left[i].time < right[j].time)):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def runSimulation():
    # Create processes based on target output
    processes = [
        Process(101, 3, "explorer.exe", 40),
        Process(102, 2, "python_script.py", 30),
        Process(103, 1, "db_service", 80),
        Process(104, 0, "anti_virus_scan", 120),
        Process(105, 5, "idle_task", 10),
        Process(106, 2, "render_video.mov", 150)
    ]
    
    # Create ready queue and add all processes
    ready_queue = Queue()
    for process in processes:
        ready_queue.enqueue(process)
    
    # Create completed stack
    completed_stack = Stack()
    
    # Display initial ready queue
    print("--- Initial Ready Queue ---")
    queue_processes = ready_queue.getAllProcesses()
    print(f"    [Queue: {', '.join(str(p) for p in queue_processes)}]")
    print()
    
    print("    --- Running Simulation ---")
    print("    Sorting processes based on priority...")
    
    # Get all processes from queue for sorting
    all_processes = []
    while not ready_queue.is_empty():
        all_processes.append(ready_queue.dequeue())
    
    # Sort processes by priority
    sorted_processes = priority_scheduler(all_processes)
    
    # Execute processes in order
    for process in sorted_processes:
        print(f"    Executing {process.task} (PID: {process.pid}, P:{process.priority}, T:{process.time})")
        completed_stack.push(process)
    
    print()
    print("    --- Simulation Complete ---")
    print("    Ready Queue is empty.")
    completed_processes = completed_stack.getAllProcesses()
    print(f"    Completed Stack: [{', '.join(str(p) for p in completed_processes)}]")
    print()
    
    print("    --- Performing Rollback ---")
    # Rollback the last completed process
    rolled_back_process = completed_stack.pop()
    print(f"    Rolled back {rolled_back_process.task} (PID: {rolled_back_process.pid}). It is now back in the ready queue.")
    ready_queue.enqueue(rolled_back_process)
    print()
    
    print("    --- Final State ---")
    final_queue_processes = ready_queue.getAllProcesses()
    print(f"    Ready Queue: [Queue: {', '.join(str(p) for p in final_queue_processes)}]")
    final_completed_processes = completed_stack.getAllProcesses()
    print(f"    Completed Stack: [{', '.join(str(p) for p in final_completed_processes)}]")

if __name__ == "__main__":
    runSimulation()